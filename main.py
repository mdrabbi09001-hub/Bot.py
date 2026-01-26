#!/usr/bin/env python3
"""
ＥＸＵ ＣＬＯＮＥＲ ＳＵＰＲＥＭＥ
Premium Website Cloner Telegram Bot
Builder: EXU Coder
"""

import os
import sys
import asyncio
import logging
import tempfile
import shutil
import zipfile
import random
import re
import json
import sqlite3
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional
import html

# Auto-install dependencies
def install_deps():
    print("\n" + "="*60)
    print("𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐢𝐧𝐠 𝐃𝐞𝐩𝐞𝐧𝐝𝐞𝐧𝐜𝐢𝐞𝐬...")
    print("="*60)
    
    deps = [
        "python-telegram-bot==20.7",
        "beautifulsoup4==4.12.2",
        "requests==2.31.0",
        "aiohttp==3.9.1",
        "aiofiles==23.2.1",
        "Pillow==10.1.0",
        "psutil==5.9.6"
    ]
    
    import subprocess
    for dep in deps:
        print(f"📦 {dep}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", dep, "-q"])
    
    print("✅ 𝐃𝐞𝐩𝐞𝐧𝐝𝐞𝐧𝐜𝐢𝐞𝐬 𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐞𝐝")
    print("="*60 + "\n")

try:
    from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
    from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler
    from telegram.constants import ParseMode
    
    import aiohttp
    from bs4 import BeautifulSoup
    import requests
    from PIL import Image, ImageDraw, ImageFont
    import qrcode
    import psutil
except ImportError:
    install_deps()
    from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
    from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler
    from telegram.constants import ParseMode
    
    import aiohttp
    from bs4 import BeautifulSoup
    import requests
    from PIL import Image, ImageDraw, ImageFont
    import qrcode
    import psutil

# ==============================================
# 𝐄𝐗𝐔 𝐅𝐎𝐍𝐓 𝐒𝐓𝐘𝐋𝐄𝐒
# ==============================================

class EXUFont:
    """EXU Font Styling System"""
    
    @staticmethod
    def bold(text: str) -> str:
        """Convert to bold text style"""
        bold_map = {
            'A': '𝐀', 'B': '𝐁', 'C': '𝐂', 'D': '𝐃', 'E': '𝐄', 'F': '𝐅', 'G': '𝐆',
            'H': '𝐇', 'I': '𝐈', 'J': '𝐉', 'K': '𝐊', 'L': '𝐋', 'M': '𝐌', 'N': '𝐍',
            'O': '𝐎', 'P': '𝐏', 'Q': '𝐐', 'R': '𝐑', 'S': '𝐒', 'T': '𝐓', 'U': '𝐔',
            'V': '𝐕', 'W': '𝐖', 'X': '𝐗', 'Y': '𝐘', 'Z': '𝐙',
            'a': '𝐚', 'b': '𝐛', 'c': '𝐜', 'd': '𝐝', 'e': '𝐞', 'f': '𝐟', 'g': '𝐠',
            'h': '𝐡', 'i': '𝐢', 'j': '𝐣', 'k': '𝐤', 'l': '𝐥', 'm': '𝐦', 'n': '𝐧',
            'o': '𝐨', 'p': '𝐩', 'q': '𝐪', 'r': '𝐫', 's': '𝐬', 't': '𝐭', 'u': '𝐮',
            'v': '𝐯', 'w': '𝐰', 'x': '𝐱', 'y': '𝐲', 'z': '𝐳',
            '0': '𝟎', '1': '𝟏', '2': '𝟐', '3': '𝟑', '4': '𝟒', '5': '𝟓',
            '6': '𝟔', '7': '𝟕', '8': '𝟖', '9': '𝟗'
        }
        return ''.join(bold_map.get(c, c) for c in text)
    
    @staticmethod
    def create_progress(progress: float, length: int = 10) -> str:
        """Create progress bar with EXU style"""
        filled = int(progress * length)
        empty = length - filled
        bars = "▰" * filled + "▱" * empty
        percent = int(progress * 100)
        
        if progress < 1.0:
            return f"⚡ {EXUFont.bold('Executing:')} [{bars}] {percent}%"
        else:
            return f"✅ {EXUFont.bold('Complete:')} [{bars}] {percent}%"
    
    @staticmethod
    def banner() -> str:
        """Create EXU banner"""
        return """
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                        ┃
┃      ███████╗██╗  ██╗██╗   ██╗    ██████╗ ██████╗     ┃
┃      ██╔════╝╚██╗██╔╝██║   ██║   ██╔════╝██╔═══██╗    ┃
┃      █████╗   ╚███╔╝ ██║   ██║   ██║     ██║   ██║    ┃
┃      ██╔══╝   ██╔██╗ ██║   ██║   ██║     ██║   ██║    ┃
┃      ███████╗██╔╝ ██╗╚██████╔╝██╗╚██████╗╚██████╔╝    ┃
┃      ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝ ╚═════╝ ╚═════╝     ┃
┃                                                        ┃
┃               𝐂𝐘𝐁𝐄𝐑 𝐂𝐋𝐎𝐍𝐄𝐑 𝐕4.0                      ┃
┃               𝐁𝐮𝐢𝐥𝐝𝐞𝐫: 𝐄𝐗𝐔 𝐂𝐨𝐝𝐞𝐫                     ┃
┃                                                        ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""
    
    @staticmethod
    def header(text: str) -> str:
        """Create header"""
        return f"\n{EXUFont.bold('═' * 50)}\n{EXUFont.bold(text.center(50))}\n{EXUFont.bold('═' * 50)}"
    
    @staticmethod
    def log(icon: str, module: str, message: str) -> str:
        """Create log message"""
        time_str = datetime.now().strftime("%H:%M:%S")
        return f"{icon} [{time_str}] [{EXUFont.bold(module)}]: {message}"

# ==============================================
# 𝐂𝐎𝐍𝐅𝐈𝐆𝐔𝐑𝐀𝐓𝐈𝐎𝐍
# ==============================================

class Config:
    TOKEN = "8398989143:AAHZWQUM0h1vHqqOCNWxh8_5bT1FbelOeoQ"
    ADMIN_IDS = [8469461108]  # Your Telegram ID
    CHANNEL_USERNAME = "@exucoder1"  # Your channel
    SUPPORT_GROUP = "@exulive"
    
    # Web scraping
    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
    ]
    
    # Limits
    MAX_CLONE_SIZE_MB = 50
    MAX_CLONES_PER_DAY = 10
    CLEANUP_MINUTES = 5

# ==============================================
# 𝐃𝐀𝐓𝐀𝐁𝐀𝐒𝐄
# ==============================================

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('exu_cloner.db', check_same_thread=False)
        self.init_db()
    
    def init_db(self):
        cursor = self.conn.cursor()
        
        # Users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT,
                join_date TEXT,
                last_active TEXT,
                is_verified INTEGER DEFAULT 0,
                is_banned INTEGER DEFAULT 0,
                clones_today INTEGER DEFAULT 0,
                total_clones INTEGER DEFAULT 0,
                last_clone_date TEXT
            )
        ''')
        
        # Clones table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                url TEXT,
                title TEXT,
                size_mb REAL,
                status TEXT,
                timestamp TEXT
            )
        ''')
        
        # Settings table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        ''')
        
        # Insert default settings
        defaults = [
            ('force_join', '1'),
            ('welcome_msg', '𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐄𝐗𝐔 𝐂𝐥𝐨𝐧𝐞𝐫!'),
            ('max_clones_per_day', '10')
        ]
        
        cursor.executemany(
            'INSERT OR IGNORE INTO settings (key, value) VALUES (?, ?)',
            defaults
        )
        
        self.conn.commit()
    
    def add_user(self, user_id: int, username: str, first_name: str):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO users 
            (user_id, username, first_name, join_date, last_active)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_id, username, first_name, 
              datetime.now().isoformat(), datetime.now().isoformat()))
        self.conn.commit()
    
    def update_activity(self, user_id: int):
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE users SET last_active = ? WHERE user_id = ?
        ''', (datetime.now().isoformat(), user_id))
        self.conn.commit()
    
    def verify_user(self, user_id: int):
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE users SET is_verified = 1 WHERE user_id = ?
        ''', (user_id,))
        self.conn.commit()
    
    def is_verified(self, user_id: int) -> bool:
        cursor = self.conn.cursor()
        cursor.execute('SELECT is_verified FROM users WHERE user_id = ?', (user_id,))
        result = cursor.fetchone()
        return result and result[0] == 1
    
    def is_banned(self, user_id: int) -> bool:
        cursor = self.conn.cursor()
        cursor.execute('SELECT is_banned FROM users WHERE user_id = ?', (user_id,))
        result = cursor.fetchone()
        return result and result[0] == 1
    
    def get_user_stats(self, user_id: int) -> Dict:
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT username, first_name, total_clones, clones_today, join_date
            FROM users WHERE user_id = ?
        ''', (user_id,))
        result = cursor.fetchone()
        
        if result:
            return {
                'username': result[0],
                'name': result[1],
                'total_clones': result[2] or 0,
                'clones_today': result[3] or 0,
                'join_date': result[4]
            }
        return {}
    
    def can_clone_today(self, user_id: int) -> bool:
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT clones_today, last_clone_date FROM users WHERE user_id = ?
        ''', (user_id,))
        result = cursor.fetchone()
        
        if not result:
            return True
        
        clones_today, last_date = result
        today = datetime.now().date().isoformat()
        
        if last_date and last_date.split('T')[0] != today:
            # Reset daily counter
            cursor.execute('''
                UPDATE users SET clones_today = 0 WHERE user_id = ?
            ''', (user_id,))
            self.conn.commit()
            return True
        
        max_clones = int(self.get_setting('max_clones_per_day', '10'))
        return clones_today < max_clones
    
    def record_clone(self, user_id: int, url: str, title: str, size_mb: float, status: str):
        cursor = self.conn.cursor()
        
        # Update user stats
        cursor.execute('''
            UPDATE users SET 
                total_clones = total_clones + 1,
                clones_today = clones_today + 1,
                last_clone_date = ?
            WHERE user_id = ?
        ''', (datetime.now().isoformat(), user_id))
        
        # Record clone
        cursor.execute('''
            INSERT INTO clones (user_id, url, title, size_mb, status, timestamp)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (user_id, url, title, size_mb, status, datetime.now().isoformat()))
        
        self.conn.commit()
    
    def get_setting(self, key: str, default: str = "") -> str:
        cursor = self.conn.cursor()
        cursor.execute('SELECT value FROM settings WHERE key = ?', (key,))
        result = cursor.fetchone()
        return result[0] if result else default
    
    def update_setting(self, key: str, value: str):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)
        ''', (key, value))
        self.conn.commit()

# ==============================================
# 𝐀𝐍𝐈𝐌𝐀𝐓𝐈𝐎𝐍 𝐄𝐍𝐆𝐈𝐍𝐄
# ==============================================

class AnimationEngine:
    """EXU Animation System"""
    
    @staticmethod
    async def progress_animation(message, text: str, duration: float = 3.0, steps: int = 10):
        """Show progress animation"""
        for i in range(steps + 1):
            progress = i / steps
            bar = EXUFont.create_progress(progress)
            
            update_text = f"""
{EXUFont.bold('𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠...')}
{bar}
{EXUFont.bold(text)}
"""
            try:
                await message.edit_text(update_text, parse_mode=ParseMode.MARKDOWN)
            except:
                pass
            
            await asyncio.sleep(duration / steps)
    
    @staticmethod
    async def typing_animation(message, texts: List[str], delay: float = 0.3):
        """Show typing animation"""
        current_text = ""
        for text in texts:
            current_text += text + "\n"
            try:
                await message.edit_text(current_text, parse_mode=ParseMode.MARKDOWN)
            except:
                pass
            await asyncio.sleep(delay)
    
    @staticmethod
    def loading_stages() -> List[str]:
        """Get loading stages"""
        return [
            "𝐈𝐧𝐢𝐭𝐢𝐚𝐥𝐢𝐳𝐢𝐧𝐠 𝐂𝐥𝐨𝐧𝐞𝐫...",
            "𝐀𝐧𝐚𝐥𝐲𝐳𝐢𝐧𝐠 𝐖𝐞𝐛𝐬𝐢𝐭𝐞...",
            "𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐀𝐬𝐬𝐞𝐭𝐬...",
            "𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐇𝐓𝐌𝐋...",
            "𝐂𝐫𝐞𝐚𝐭𝐢𝐧𝐠 𝐏𝐚𝐜𝐤𝐚𝐠𝐞..."
        ]

# ==============================================
# 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐕𝐄𝐑𝐈𝐅𝐈𝐂𝐀𝐓𝐈𝐎𝐍
# ==============================================

class ChannelVerification:
    @staticmethod
    async def check_membership(bot, user_id: int, channel: str) -> bool:
        """Check if user is member of channel"""
        try:
            # Try to get chat member
            chat_member = await bot.get_chat_member(channel, user_id)
            return chat_member.status in ['member', 'administrator', 'creator']
        except:
            return False
    
    @staticmethod
    def get_join_message() -> tuple:
        """Get channel join message"""
        message = f"""
{EXUFont.bold('𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐕𝐄𝐑𝐈𝐅𝐈𝐂𝐀𝐓𝐈𝐎𝐍 𝐑𝐄𝐐𝐔𝐈𝐑𝐄𝐃')}

📢 𝐉𝐨𝐢𝐧 𝐨𝐮𝐫 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐭𝐨 𝐮𝐬𝐞 𝐭𝐡𝐢𝐬 𝐛𝐨𝐭:
{Config.CHANNEL_USERNAME}

💬 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩:
{Config.SUPPORT_GROUP}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
𝐈𝐧𝐬𝐭𝐫𝐮𝐜𝐭𝐢𝐨𝐧𝐬:
1. 𝐂𝐥𝐢𝐜𝐤 𝐉𝐨𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐛𝐮𝐭𝐭𝐨𝐧
2. 𝐉𝐨𝐢𝐧 𝐭𝐡𝐞 𝐜𝐡𝐚𝐧𝐧𝐞𝐥
3. 𝐂𝐥𝐢𝐜𝐤 "✅ 𝐈'𝐯𝐞 𝐉𝐨𝐢𝐧𝐞𝐝"
4. 𝐁𝐨𝐭 𝐰𝐢𝐥𝐥 𝐯𝐞𝐫𝐢𝐟𝐲 𝐲𝐨𝐮𝐫 𝐦𝐞𝐦𝐛𝐞𝐫𝐬𝐡𝐢𝐩
"""
        
        keyboard = [
            [InlineKeyboardButton("📢 𝐉𝐨𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url=f"https://t.me/{Config.CHANNEL_USERNAME.lstrip('@')}")],
            [InlineKeyboardButton("💬 𝐉𝐨𝐢𝐧 𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url=f"https://t.me/{Config.SUPPORT_GROUP.lstrip('@')}")],
            [InlineKeyboardButton("✅ 𝐈'𝐯𝐞 𝐉𝐨𝐢𝐧𝐞𝐝", callback_data="verify_join")]
        ]
        
        return message, InlineKeyboardMarkup(keyboard)

# ==============================================
# 𝐖𝐄𝐁𝐒𝐈𝐓𝐄 𝐂𝐋𝐎𝐍𝐄𝐑
# ==============================================

class WebsiteCloner:
    def __init__(self):
        self.temp_dir = None
        self.session = None
    
    async def initialize(self):
        """Initialize cloner"""
        self.temp_dir = tempfile.mkdtemp(prefix="exu_clone_")
        self.session = aiohttp.ClientSession()
        return self
    
    async def clone_website(self, url: str) -> Dict:
        """Clone a website"""
        try:
            # Fetch website
            headers = {'User-Agent': random.choice(Config.USER_AGENTS)}
            
            async with self.session.get(url, headers=headers, timeout=30) as response:
                html_content = await response.text()
            
            # Parse HTML
            soup = BeautifulSoup(html_content, 'html.parser')
            title = soup.title.string if soup.title else "Website Clone"
            
            # Extract resources
            resources = []
            
            # CSS files
            for link in soup.find_all('link', rel='stylesheet'):
                if link.get('href'):
                    resources.append(('css', link['href']))
            
            # JS files
            for script in soup.find_all('script', src=True):
                resources.append(('js', script['src']))
            
            # Images
            for img in soup.find_all('img', src=True):
                resources.append(('img', img['src']))
            
            # Create package
            package_dir = os.path.join(self.temp_dir, "website")
            os.makedirs(package_dir, exist_ok=True)
            
            # Save HTML
            html_file = os.path.join(package_dir, "index.html")
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            
            # Download resources
            assets_dir = os.path.join(package_dir, "assets")
            os.makedirs(assets_dir, exist_ok=True)
            
            downloaded = 0
            for i, (rtype, resource_url) in enumerate(resources[:20]):  # Limit to 20 resources
                try:
                    # Fix URL
                    if resource_url.startswith('//'):
                        resource_url = 'https:' + resource_url
                    elif resource_url.startswith('/'):
                        resource_url = url.rstrip('/') + resource_url
                    elif not resource_url.startswith(('http://', 'https://')):
                        resource_url = url.rstrip('/') + '/' + resource_url.lstrip('/')
                    
                    # Download
                    async with self.session.get(resource_url, timeout=10) as res:
                        if res.status == 200:
                            content = await res.read()
                            ext = resource_url.split('.')[-1].split('?')[0] if '.' in resource_url else 'bin'
                            filename = f"{i:03d}.{ext}"
                            filepath = os.path.join(assets_dir, filename)
                            
                            with open(filepath, 'wb') as f:
                                f.write(content)
                            downloaded += 1
                except:
                    continue
            
            # Create ZIP
            zip_path = os.path.join(self.temp_dir, "website_clone.zip")
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(package_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, package_dir)
                        zipf.write(file_path, arcname)
            
            file_size = os.path.getsize(zip_path) / (1024 * 1024)
            
            return {
                'success': True,
                'title': title,
                'zip_path': zip_path,
                'file_size': file_size,
                'resources_found': len(resources),
                'resources_downloaded': downloaded
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    async def cleanup(self):
        """Cleanup resources"""
        if self.session:
            await self.session.close()
        
        # Schedule cleanup
        async def delayed_cleanup():
            await asyncio.sleep(Config.CLEANUP_MINUTES * 60)
            try:
                if self.temp_dir and os.path.exists(self.temp_dir):
                    shutil.rmtree(self.temp_dir)
            except:
                pass
        
        asyncio.create_task(delayed_cleanup())

# ==============================================
# 𝐌𝐀𝐈𝐍 𝐁𝐎𝐓 𝐂𝐋𝐀𝐒𝐒
# ==============================================

class EXUClonerBot:
    def __init__(self):
        self.app = None
        self.db = Database()
        self.active_clones = {}
        self.start_time = datetime.now()
        
        print(EXUFont.banner())
        print(f"Builder: EXU Coder | Supreme Edition")
        print(f"Start Time: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*60 + "\n")
    
    # ==============================================
    # 𝐌𝐄𝐍𝐔 𝐒𝐘𝐒𝐓𝐄𝐌
    # ==============================================
    
    def main_menu(self, user_id: int = None) -> InlineKeyboardMarkup:
        """Main menu buttons"""
        keyboard = [
            [InlineKeyboardButton("🚀 𝐂𝐥𝐨𝐧𝐞 𝐖𝐞𝐛𝐬𝐢𝐭𝐞", callback_data="clone_site")],
            [
                InlineKeyboardButton("📊 𝐌𝐲 𝐏𝐫𝐨𝐟𝐢𝐥𝐞", callback_data="my_profile"),
                InlineKeyboardButton("⚡ 𝐒𝐭𝐚𝐭𝐮𝐬", callback_data="bot_status")
            ],
            [
                InlineKeyboardButton("ℹ️ 𝐀𝐛𝐨𝐮𝐭", callback_data="about_bot"),
                InlineKeyboardButton("🆘 𝐇𝐞𝐥𝐩", callback_data="help_menu")
            ]
        ]
        
        # Add admin button for admins
        if user_id in Config.ADMIN_IDS:
            keyboard.append([InlineKeyboardButton("👑 𝐀𝐝𝐦𝐢𝐧 𝐏𝐚𝐧𝐞𝐥", callback_data="admin_panel")])
        
        # Add verify button if not verified
        if user_id and not self.db.is_verified(user_id):
            keyboard.append([InlineKeyboardButton("🛡️ 𝐕𝐞𝐫𝐢𝐟𝐲 𝐉𝐨𝐢𝐧", callback_data="verify_join")])
        
        return InlineKeyboardMarkup(keyboard)
    
    def admin_menu(self) -> InlineKeyboardMarkup:
        """Admin panel menu"""
        keyboard = [
            [InlineKeyboardButton("👥 𝐔𝐬𝐞𝐫 𝐌𝐚𝐧𝐚𝐠𝐞𝐦𝐞𝐧𝐭", callback_data="admin_users")],
            [InlineKeyboardButton("📊 𝐁𝐨𝐭 𝐒𝐭𝐚𝐭𝐬", callback_data="admin_stats")],
            [InlineKeyboardButton("⚙️ 𝐁𝐨𝐭 𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬", callback_data="admin_settings")],
            [InlineKeyboardButton("📢 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭", callback_data="admin_broadcast")],
            [InlineKeyboardButton("◀️ 𝐁𝐚𝐜𝐤 𝐭𝐨 𝐌𝐚𝐢𝐧", callback_data="main_menu")]
        ]
        return InlineKeyboardMarkup(keyboard)
    
    # ==============================================
    # 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 𝐇𝐀𝐍𝐃𝐋𝐄𝐑𝐒
    # ==============================================
    
    async def start_command(self, update: Update, context: CallbackContext):
        """Handle /start command"""
        user = update.effective_user
        
        # Add user to database
        self.db.add_user(user.id, user.username or "", user.first_name or "")
        self.db.update_activity(user.id)
        
        # Check if banned
        if self.db.is_banned(user.id):
            await update.message.reply_text(
                f"❌ {EXUFont.bold('𝐀𝐜𝐜𝐞𝐬𝐬 𝐃𝐞𝐧𝐢𝐞𝐝')}\n\n"
                f"𝐘𝐨𝐮𝐫 𝐚𝐜𝐜𝐨𝐮𝐧𝐭 𝐡𝐚𝐬 𝐛𝐞𝐞𝐧 𝐛𝐚𝐧𝐧𝐞𝐝 𝐟𝐫𝐨𝐦 𝐮𝐬𝐢𝐧𝐠 𝐭𝐡𝐢𝐬 𝐛𝐨𝐭.",
                parse_mode=ParseMode.MARKDOWN
            )
            return
        
        # Check channel verification
        force_join = self.db.get_setting('force_join', '1') == '1'
        if force_join and not self.db.is_verified(user.id):
            join_msg, keyboard = ChannelVerification.get_join_message()
            await update.message.reply_text(
                join_msg,
                reply_markup=keyboard,
                parse_mode=ParseMode.MARKDOWN
            )
            return
        
        # Show welcome message
        welcome_msg = self.db.get_setting('welcome_msg', '𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐄𝐗𝐔 𝐂𝐥𝐨𝐧𝐞𝐫!')
        
        message = f"""
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐄𝐗𝐔 𝐂𝐋𝐎𝐍𝐄𝐑')}
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}

👤 𝐔𝐬𝐞𝐫: {user.first_name}
🆔 𝐈𝐃: {user.id}
📅 𝐃𝐚𝐭𝐞: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

{welcome_msg}

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐀𝐕𝐀𝐈𝐋𝐀𝐁𝐋𝐄 𝐅𝐄𝐀𝐓𝐔𝐑𝐄𝐒')}
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}

🚀 𝐂𝐥𝐨𝐧𝐞 𝐖𝐞𝐛𝐬𝐢𝐭𝐞 - 𝐂𝐥𝐨𝐧𝐞 𝐚𝐧𝐲 𝐰𝐞𝐛𝐬𝐢𝐭𝐞
📊 𝐌𝐲 𝐏𝐫𝐨𝐟𝐢𝐥𝐞 - 𝐕𝐢𝐞𝐰 𝐲𝐨𝐮𝐫 𝐬𝐭𝐚𝐭𝐬
⚡ 𝐒𝐭𝐚𝐭𝐮𝐬 - 𝐁𝐨𝐭 𝐬𝐭𝐚𝐭𝐮𝐬 & 𝐢𝐧𝐟𝐨
ℹ️ 𝐀𝐛𝐨𝐮𝐭 - 𝐀𝐛𝐨𝐮𝐭 𝐄𝐗𝐔 𝐂𝐥𝐨𝐧𝐞𝐫
🆘 𝐇𝐞𝐥𝐩 - 𝐆𝐞𝐭 𝐡𝐞𝐥𝐩 & 𝐬𝐮𝐩𝐩𝐨𝐫𝐭

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐁𝐮𝐢𝐥𝐝𝐞𝐫: 𝐄𝐗𝐔 𝐂𝐨𝐝𝐞𝐫')}
"""
        
        await update.message.reply_text(
            message,
            reply_markup=self.main_menu(user.id),
            parse_mode=ParseMode.MARKDOWN
        )
    
    async def callback_handler(self, update: Update, context: CallbackContext):
        """Handle callback queries"""
        query = update.callback_query
        await query.answer()
        
        user_id = query.from_user.id
        data = query.data
        
        print(EXUFont.log("📱", "BUTTON", f"User {user_id} pressed: {data}"))
        
        # Update activity
        self.db.update_activity(user_id)
        
        # Handle callbacks
        if data == "main_menu":
            await self.show_main_menu(query)
        elif data == "verify_join":
            await self.verify_user(query, context)
        elif data == "clone_site":
            await self.start_cloning(query)
        elif data == "my_profile":
            await self.show_profile(query, user_id)
        elif data == "bot_status":
            await self.show_bot_status(query)
        elif data == "about_bot":
            await self.show_about(query)
        elif data == "help_menu":
            await self.show_help(query)
        elif data == "admin_panel":
            await self.show_admin_panel(query, user_id)
        elif data.startswith("admin_"):
            await self.handle_admin_callback(query, context, data, user_id)
        else:
            await query.answer("⚡ 𝐅𝐞𝐚𝐭𝐮𝐫𝐞 𝐜𝐨𝐦𝐢𝐧𝐠 𝐬𝐨𝐨𝐧!", show_alert=True)
    
    # ==============================================
    # 𝐔𝐒𝐄𝐑 𝐅𝐄𝐀𝐓𝐔𝐑𝐄𝐒
    # ==============================================
    
    async def show_main_menu(self, query):
        """Show main menu"""
        user_id = query.from_user.id
        user_stats = self.db.get_user_stats(user_id)
        
        menu_text = f"""
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐄𝐗𝐔 𝐂𝐋𝐎𝐍𝐄𝐑 𝐌𝐀𝐈𝐍 𝐌𝐄𝐍𝐔')}
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}

👤 𝐔𝐬𝐞𝐫: {user_stats.get('name', 'User')}
📊 𝐂𝐥𝐨𝐧𝐞𝐬 𝐓𝐨𝐝𝐚𝐲: {user_stats.get('clones_today', 0)}/{self.db.get_setting('max_clones_per_day', '10')}
🏆 𝐓𝐨𝐭𝐚𝐥 𝐂𝐥𝐨𝐧𝐞𝐬: {user_stats.get('total_clones', 0)}

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐒𝐄𝐋𝐄𝐂𝐓 𝐀𝐍 𝐎𝐏𝐓𝐈𝐎𝐍:')}
"""
        
        await query.edit_message_text(
            menu_text,
            reply_markup=self.main_menu(user_id),
            parse_mode=ParseMode.MARKDOWN
        )
    
    async def verify_user(self, query, context: CallbackContext):
        """Verify user has joined channel"""
        user_id = query.from_user.id
        
        # Show checking animation
        await query.edit_message_text(
            f"{EXUFont.bold('𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬𝐡𝐢𝐩...')}\n\n"
            f"⚡ {EXUFont.bold('𝐏𝐥𝐞𝐚𝐬𝐞 𝐰𝐚𝐢𝐭...')}",
            parse_mode=ParseMode.MARKDOWN
        )
        
        # Check membership
        is_member = await ChannelVerification.check_membership(
            context.bot, user_id, Config.CHANNEL_USERNAME
        )
        
        if is_member:
            # Mark as verified
            self.db.verify_user(user_id)
            
            await query.edit_message_text(
                f"✅ {EXUFont.bold('𝐕𝐄𝐑𝐈𝐅𝐈𝐂𝐀𝐓𝐈𝐎𝐍 𝐒𝐔𝐂𝐂𝐄𝐒𝐒!')}\n\n"
                f"𝐓𝐡𝐚𝐧𝐤 𝐲𝐨𝐮 𝐟𝐨𝐫 𝐣𝐨𝐢𝐧𝐢𝐧𝐠 {Config.CHANNEL_USERNAME}!\n"
                f"𝐘𝐨𝐮 𝐧𝐨𝐰 𝐡𝐚𝐯𝐞 𝐟𝐮𝐥𝐥 𝐚𝐜𝐜𝐞𝐬𝐬 𝐭𝐨 𝐄𝐗𝐔 𝐂𝐥𝐨𝐧𝐞𝐫.",
                reply_markup=self.main_menu(user_id),
                parse_mode=ParseMode.MARKDOWN
            )
        else:
            # Show join message again
            join_msg, keyboard = ChannelVerification.get_join_message()
            await query.edit_message_text(
                f"❌ {EXUFont.bold('𝐕𝐄𝐑𝐈𝐅𝐈𝐂𝐀𝐓𝐈𝐎𝐍 𝐅𝐀𝐈𝐋𝐄𝐃')}\n\n"
                f"𝐏𝐥𝐞𝐚𝐬𝐞 𝐣𝐨𝐢𝐧 {Config.CHANNEL_USERNAME} 𝐟𝐢𝐫𝐬𝐭.\n"
                f"𝐂𝐥𝐢𝐜𝐤 𝐭𝐡𝐞 𝐛𝐮𝐭𝐭𝐨𝐧 𝐛𝐞𝐥𝐨𝐰 𝐭𝐨 𝐣𝐨𝐢𝐧 𝐚𝐧𝐝 𝐭𝐫𝐲 𝐚𝐠𝐚𝐢𝐧.",
                reply_markup=keyboard,
                parse_mode=ParseMode.MARKDOWN
            )
    
    async def start_cloning(self, query):
        """Start cloning process"""
        user_id = query.from_user.id
        
        # Check verification
        force_join = self.db.get_setting('force_join', '1') == '1'
        if force_join and not self.db.is_verified(user_id):
            join_msg, keyboard = ChannelVerification.get_join_message()
            await query.edit_message_text(
                join_msg,
                reply_markup=keyboard,
                parse_mode=ParseMode.MARKDOWN
            )
            return
        
        # Check daily limit
        if not self.db.can_clone_today(user_id):
            max_clones = self.db.get_setting('max_clones_per_day', '10')
            await query.answer(
                f"❌ 𝐃𝐚𝐢𝐥𝐲 𝐥𝐢𝐦𝐢𝐭 𝐫𝐞𝐚𝐜𝐡𝐞𝐝! ({max_clones}/{max_clones})",
                show_alert=True
            )
            return
        
        await query.edit_message_text(
            f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
            f"{EXUFont.bold('𝐂𝐋𝐎𝐍𝐄 𝐖𝐄𝐁𝐒𝐈𝐓𝐄')}\n"
            f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n\n"
            f"📝 {EXUFont.bold('𝐏𝐥𝐞𝐚𝐬𝐞 𝐬𝐞𝐧𝐝 𝐭𝐡𝐞 𝐔𝐑𝐋 𝐲𝐨𝐮 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐜𝐥𝐨𝐧𝐞:')}\n\n"
            f"𝐄𝐱𝐚𝐦𝐩𝐥𝐞𝐬:\n"
            f"• https://example.com\n"
            f"• https://github.com\n"
            f"• https://wikipedia.org\n\n"
            f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
            f"⚠️ {EXUFont.bold('𝐋𝐢𝐦𝐢𝐭𝐬:')}\n"
            f"• 𝐌𝐚𝐱 𝐟𝐢𝐥𝐞 𝐬𝐢𝐳𝐞: {Config.MAX_CLONE_SIZE_MB} MB\n"
            f"• 𝐂𝐥𝐨𝐧𝐞𝐬 𝐭𝐨𝐝𝐚𝐲: {self.db.get_user_stats(user_id).get('clones_today', 0)}/{self.db.get_setting('max_clones_per_day', '10')}",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("◀️ 𝐂𝐚𝐧𝐜𝐞𝐥", callback_data="main_menu")]
            ]),
            parse_mode=ParseMode.MARKDOWN
        )
        
        # Store that we're waiting for URL
        self.active_clones[user_id] = {"state": "waiting_url"}
    
    async def handle_url_message(self, update: Update, context: CallbackContext):
        """Handle URL messages for cloning"""
        user_id = update.effective_user.id
        
        if user_id in self.active_clones and self.active_clones[user_id].get("state") == "waiting_url":
            url = update.message.text.strip()
            
            # Validate URL
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url
            
            # Start cloning
            await self.process_clone(update, url, user_id)
        else:
            # Send to main menu
            await self.start_command(update, context)
    
    async def process_clone(self, update: Update, url: str, user_id: int):
        """Process website cloning"""
        # Create status message
        status_msg = await update.message.reply_text(
            f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
            f"{EXUFont.bold('𝐂𝐋𝐎𝐍𝐈𝐍𝐆 𝐒𝐓𝐀𝐑𝐓𝐄𝐃')}\n"
            f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n\n"
            f"🔗 𝐔𝐑𝐋: {url[:50]}...\n"
            f"👤 𝐔𝐬𝐞𝐫: {update.effective_user.first_name}\n\n"
            f"⚡ {EXUFont.bold('𝐄𝐱𝐞𝐜𝐮𝐭𝐢𝐧𝐠:')} [▱▱▱▱▱▱▱▱▱▱] 0%\n\n"
            f"𝐏𝐥𝐞𝐚𝐬𝐞 𝐰𝐚𝐢𝐭, 𝐭𝐡𝐢𝐬 𝐦𝐚𝐲 𝐭𝐚𝐤𝐞 𝐚 𝐟𝐞𝐰 𝐦𝐢𝐧𝐮𝐭𝐞𝐬...",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("❌ 𝐂𝐚𝐧𝐜𝐞𝐥", callback_data=f"cancel_{user_id}")]
            ]),
            parse_mode=ParseMode.MARKDOWN
        )
        
        # Start clone task
        task = asyncio.create_task(
            self.execute_clone(update, url, status_msg, user_id)
        )
        self.active_clones[user_id] = {
            "task": task,
            "url": url,
            "start_time": datetime.now(),
            "status_msg": status_msg
        }
    
    async def execute_clone(self, update: Update, url: str, status_msg, user_id: int):
        """Execute the cloning process"""
        cloner = None
        
        try:
            # Initialize cloner
            await self.update_status(status_msg, "𝐈𝐧𝐢𝐭𝐢𝐚𝐥𝐢𝐳𝐢𝐧𝐠 𝐂𝐥𝐨𝐧𝐞𝐫...", 0.1)
            cloner = await WebsiteCloner().initialize()
            
            # Clone website
            await self.update_status(status_msg, "𝐀𝐧𝐚𝐥𝐲𝐳𝐢𝐧𝐠 𝐖𝐞𝐛𝐬𝐢𝐭𝐞...", 0.3)
            result = await cloner.clone_website(url)
            
            if not result['success']:
                await self.update_status(status_msg, f"𝐄𝐫𝐫𝐨𝐫: {result['error'][:100]}", 0, error=True)
                self.db.record_clone(user_id, url, "Failed", 0, "failed")
                return
            
            await self.update_status(status_msg, "𝐂𝐫𝐞𝐚𝐭𝐢𝐧𝐠 𝐏𝐚𝐜𝐤𝐚𝐠𝐞...", 0.8)
            await self.update_status(status_msg, "𝐅𝐢𝐧𝐚𝐥𝐢𝐳𝐢𝐧𝐠...", 0.9)
            
            # Record success
            self.db.record_clone(
                user_id, 
                url, 
                result['title'], 
                result['file_size'], 
                "success"
            )
            
            # Send success message
            time_taken = (datetime.now() - self.active_clones[user_id]['start_time']).total_seconds()
            
            await status_msg.edit_text(
                f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
                f"✅ {EXUFont.bold('𝐂𝐋𝐎𝐍𝐈𝐍𝐆 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄!')}\n"
                f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n\n"
                f"📄 𝐓𝐢𝐭𝐥𝐞: {result['title'][:50]}\n"
                f"🔗 𝐔𝐑𝐋: {url[:50]}...\n"
                f"📦 𝐅𝐢𝐥𝐞 𝐒𝐢𝐳𝐞: {result['file_size']:.2f} MB\n"
                f"📊 𝐑𝐞𝐬𝐨𝐮𝐫𝐜𝐞𝐬: {result['resources_downloaded']}/{result['resources_found']}\n"
                f"⏱️ 𝐓𝐢𝐦𝐞: {time_taken:.1f}𝐬\n\n"
                f"✅ {EXUFont.bold('𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞:')} [▰▰▰▰▰▰▰▰▰▰] 100%\n\n"
                f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
                f"📦 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐭𝐡𝐞 𝐳𝐢𝐩 𝐟𝐢𝐥𝐞 𝐛𝐞𝐥𝐨𝐰:",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("🔄 𝐍𝐞𝐰 𝐂𝐥𝐨𝐧𝐞", callback_data="clone_site")],
                    [InlineKeyboardButton("🏠 𝐌𝐚𝐢𝐧 𝐌𝐞𝐧𝐮", callback_data="main_menu")]
                ]),
                parse_mode=ParseMode.MARKDOWN
            )
            
            # Send ZIP file
            with open(result['zip_path'], 'rb') as f:
                await update.message.reply_document(
                    document=f,
                    filename=f"exu_clone_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip",
                    caption=f"📦 𝐄𝐗𝐔 𝐂𝐥𝐨𝐧𝐞 - {result['title'][:50]}",
                    reply_markup=self.main_menu(user_id)
                )
            
        except Exception as e:
            # Record failure
            self.db.record_clone(user_id, url, "Failed", 0, "failed")
            
            await status_msg.edit_text(
                f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
                f"❌ {EXUFont.bold('𝐂𝐋𝐎𝐍𝐈𝐍𝐆 𝐅𝐀𝐈𝐋𝐄𝐃')}\n"
                f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n\n"
                f"🔗 𝐔𝐑𝐋: {url[:50]}...\n"
                f"💥 𝐄𝐫𝐫𝐨𝐫: {str(e)[:100]}...\n\n"
                f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
                f"⚠️ {EXUFont.bold('𝐓𝐫𝐲 𝐭𝐡𝐞𝐬𝐞:')}\n"
                f"• 𝐔𝐬𝐞 𝐚 𝐬𝐢𝐦𝐩𝐥𝐞𝐫 𝐰𝐞𝐛𝐬𝐢𝐭𝐞\n"
                f"• 𝐂𝐡𝐞𝐜𝐤 𝐭𝐡𝐞 𝐔𝐑𝐋 𝐢𝐬 𝐜𝐨𝐫𝐫𝐞𝐜𝐭\n"
                f"• 𝐓𝐫𝐲 𝐚𝐠𝐚𝐢𝐧 𝐥𝐚𝐭𝐞𝐫",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("🔄 𝐓𝐫𝐲 𝐀𝐠𝐚𝐢𝐧", callback_data="clone_site")],
                    [InlineKeyboardButton("🏠 𝐌𝐚𝐢𝐧 𝐌𝐞𝐧𝐮", callback_data="main_menu")]
                ]),
                parse_mode=ParseMode.MARKDOWN
            )
            
            print(EXUFont.log("❌", "CLONER", f"Clone failed: {str(e)[:100]}"))
            
        finally:
            if cloner:
                await cloner.cleanup()
            if user_id in self.active_clones:
                del self.active_clones[user_id]
    
    async def update_status(self, message, text: str, progress: float, error: bool = False):
        """Update status message with progress"""
        bar = EXUFont.create_progress(progress)
        
        try:
            if not error:
                await message.edit_text(
                    f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
                    f"{EXUFont.bold('𝐂𝐋𝐎𝐍𝐈𝐍𝐆 𝐈𝐍 𝐏𝐑𝐎𝐆𝐑𝐄𝐒𝐒')}\n"
                    f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n\n"
                    f"{bar}\n"
                    f"{text}\n\n"
                    f"𝐏𝐥𝐞𝐚𝐬𝐞 𝐰𝐚𝐢𝐭, 𝐝𝐨 𝐧𝐨𝐭 𝐜𝐥𝐨𝐬𝐞 𝐭𝐡𝐞 𝐚𝐩𝐩...",
                    parse_mode=ParseMode.MARKDOWN
                )
            else:
                await message.edit_text(
                    f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
                    f"❌ {EXUFont.bold('𝐂𝐋𝐎𝐍𝐈𝐍𝐆 𝐅𝐀𝐈𝐋𝐄𝐃')}\n"
                    f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n\n"
                    f"{text}\n\n"
                    f"❌ {EXUFont.bold('𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐟𝐚𝐢𝐥𝐞𝐝!')}",
                    parse_mode=ParseMode.MARKDOWN
                )
        except:
            pass
        
        # Animation delay
        await asyncio.sleep(0.5)
    
    async def show_profile(self, query, user_id: int):
        """Show user profile"""
        user_stats = self.db.get_user_stats(user_id)
        verified = self.db.is_verified(user_id)
        
        profile_text = f"""
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐌𝐘 𝐏𝐑𝐎𝐅𝐈𝐋𝐄')}
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}

👤 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞: @{user_stats.get('username', 'N/A')}
📛 𝐍𝐚𝐦𝐞: {user_stats.get('name', 'User')}
🆔 𝐈𝐃: {user_id}
📅 𝐉𝐨𝐢𝐧𝐞𝐝: {user_stats.get('join_date', 'N/A')}
🛡️ 𝐒𝐭𝐚𝐭𝐮𝐬: {'✅ 𝐕𝐞𝐫𝐢𝐟𝐢𝐞𝐝' if verified else '⭕ 𝐏𝐞𝐧𝐝𝐢𝐧𝐠'}

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐂𝐋𝐎𝐍𝐈𝐍𝐆 𝐒𝐓𝐀𝐓𝐒')}

📊 𝐓𝐨𝐭𝐚𝐥 𝐂𝐥𝐨𝐧𝐞𝐬: {user_stats.get('total_clones', 0)}
📈 𝐂𝐥𝐨𝐧𝐞𝐬 𝐓𝐨𝐝𝐚𝐲: {user_stats.get('clones_today', 0)}/{self.db.get_setting('max_clones_per_day', '10')}
🎯 𝐒𝐮𝐜𝐜𝐞𝐬𝐬 𝐑𝐚𝐭𝐞: {((user_stats.get('total_clones', 0) / max(user_stats.get('total_clones', 1), 1)) * 100):.1f}%

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐀𝐂𝐓𝐈𝐎𝐍𝐒')}
"""
        
        keyboard = [[InlineKeyboardButton("🔄 𝐑𝐞𝐟𝐫𝐞𝐬𝐡", callback_data="my_profile")]]
        if not verified:
            keyboard.append([InlineKeyboardButton("🛡️ 𝐕𝐞𝐫𝐢𝐟𝐲 𝐉𝐨𝐢𝐧", callback_data="verify_join")])
        keyboard.append([InlineKeyboardButton("◀️ 𝐁𝐚𝐜𝐤", callback_data="main_menu")])
        
        await query.edit_message_text(
            profile_text,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode=ParseMode.MARKDOWN
        )
    
    async def show_bot_status(self, query):
        """Show bot status"""
        uptime = datetime.now() - self.start_time
        hours, remainder = divmod(int(uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        
        # Get bot stats
        cursor = self.db.conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM users')
        total_users = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM clones WHERE status = "success"')
        total_clones = cursor.fetchone()[0]
        
        status_text = f"""
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐁𝐎𝐓 𝐒𝐓𝐀𝐓𝐔𝐒')}
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}

🤖 𝐁𝐨𝐭: 𝐄𝐗𝐔 𝐂𝐥𝐨𝐧𝐞𝐫 v4.0
⚡ 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐎𝐧𝐥𝐢𝐧𝐞
⏱️ 𝐔𝐩𝐭𝐢𝐦𝐞: {hours}h {minutes}m {seconds}s
💾 𝐌𝐞𝐦𝐨𝐫𝐲: {psutil.Process().memory_info().rss / 1024 / 1024:.1f} MB

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐒𝐓𝐀𝐓𝐈𝐒𝐓𝐈𝐂𝐒')}

👥 𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫𝐬: {total_users}
🚀 𝐓𝐨𝐭𝐚𝐥 𝐂𝐥𝐨𝐧𝐞𝐬: {total_clones}
⚡ 𝐀𝐜𝐭𝐢𝐯𝐞 𝐂𝐥𝐨𝐧𝐞𝐬: {len(self.active_clones)}

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐒𝐄𝐓𝐓𝐈𝐍𝐆𝐒')}

📢 𝐂𝐡𝐚𝐧𝐧𝐞𝐥: {Config.CHANNEL_USERNAME}
🛡️ 𝐕𝐞𝐫𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧: {'✅ 𝐎𝐧' if self.db.get_setting('force_join', '1') == '1' else '❌ 𝐎𝐟𝐟'}
📊 𝐃𝐚𝐢𝐥𝐲 𝐋𝐢𝐦𝐢𝐭: {self.db.get_setting('max_clones_per_day', '10')}
"""
        
        await query.edit_message_text(
            status_text,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔄 𝐑𝐞𝐟𝐫𝐞𝐬𝐡", callback_data="bot_status")],
                [InlineKeyboardButton("◀️ 𝐁𝐚𝐜𝐤", callback_data="main_menu")]
            ]),
            parse_mode=ParseMode.MARKDOWN
        )
    
    async def show_about(self, query):
        """Show about information"""
        about_text = f"""
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐀𝐁𝐎𝐔𝐓 𝐄𝐗𝐔 𝐂𝐋𝐎𝐍𝐄𝐑')}
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}

🚀 𝐄𝐗𝐔 𝐂𝐋𝐎𝐍𝐄𝐑 v4.0
🎯 𝐀𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐖𝐞𝐛𝐬𝐢𝐭𝐞 𝐂𝐥𝐨𝐧𝐞𝐫

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐅𝐄𝐀𝐓𝐔𝐑𝐄𝐒')}

✅ 𝐂𝐥𝐨𝐧𝐞 𝐚𝐧𝐲 𝐰𝐞𝐛𝐬𝐢𝐭𝐞
✅ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐚𝐥𝐥 𝐚𝐬𝐬𝐞𝐭𝐬
✅ 𝐂𝐫𝐞𝐚𝐭𝐞 𝐙𝐈𝐏 𝐩𝐚𝐜𝐤𝐚𝐠𝐞𝐬
✅ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐯𝐞𝐫𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧
✅ 𝐔𝐬𝐞𝐫 𝐦𝐚𝐧𝐚𝐠𝐞𝐦𝐞𝐧𝐭
✅ 𝐀𝐝𝐦𝐢𝐧 𝐩𝐚𝐧𝐞𝐥

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐂𝐑𝐄𝐀𝐓𝐎𝐑')}

👨‍💻 𝐁𝐮𝐢𝐥𝐝𝐞𝐫: 𝐄𝐗𝐔 𝐂𝐨𝐝𝐞𝐫
⚡ 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐁𝐨𝐭𝐬
🎯 𝐇𝐢𝐠𝐡-𝐏𝐞𝐫𝐟𝐨𝐫𝐦𝐚𝐧𝐜𝐞 𝐒𝐨𝐥𝐮𝐭𝐢𝐨𝐧𝐬

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐒𝐔𝐏𝐏𝐎𝐑𝐓')}

💬 𝐒𝐮𝐩𝐩𝐨𝐫𝐭: {Config.SUPPORT_GROUP}
📢 𝐂𝐡𝐚𝐧𝐧𝐞𝐥: {Config.CHANNEL_USERNAME}
"""
        
        await query.edit_message_text(
            about_text,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("◀️ 𝐁𝐚𝐜𝐤", callback_data="main_menu")]
            ]),
            parse_mode=ParseMode.MARKDOWN
        )
    
    async def show_help(self, query):
        """Show help information"""
        help_text = f"""
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐇𝐄𝐋𝐏 & 𝐒𝐔𝐏𝐏𝐎𝐑𝐓')}
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}

📚 𝐇𝐎𝐖 𝐓𝐎 𝐔𝐒𝐄:

1. 𝐉𝐨𝐢𝐧 𝐭𝐡𝐞 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝 𝐜𝐡𝐚𝐧𝐧𝐞𝐥
2. 𝐕𝐞𝐫𝐢𝐟𝐲 𝐲𝐨𝐮𝐫 𝐦𝐞𝐦𝐛𝐞𝐫𝐬𝐡𝐢𝐩
3. 𝐂𝐥𝐢𝐜𝐤 "𝐂𝐥𝐨𝐧𝐞 𝐖𝐞𝐛𝐬𝐢𝐭𝐞"
4. 𝐒𝐞𝐧𝐝 𝐭𝐡𝐞 𝐔𝐑𝐋 𝐲𝐨𝐮 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐜𝐥𝐨𝐧𝐞
5. 𝐖𝐚𝐢𝐭 𝐟𝐨𝐫 𝐩𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠
6. 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐭𝐡𝐞 𝐙𝐈𝐏 𝐟𝐢𝐥𝐞

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐓𝐑𝐎𝐔𝐁𝐋𝐄𝐒𝐇𝐎𝐎𝐓𝐈𝐍𝐆')}

❌ 𝐂𝐚𝐧'𝐭 𝐜𝐥𝐨𝐧𝐞: 𝐓𝐫𝐲 𝐬𝐢𝐦𝐩𝐥𝐞𝐫 𝐬𝐢𝐭𝐞𝐬
⏳ 𝐓𝐢𝐦𝐞𝐨𝐮𝐭: 𝐂𝐡𝐞𝐜𝐤 𝐢𝐧𝐭𝐞𝐫𝐧𝐞𝐭
💾 𝐍𝐨 𝐬𝐭𝐨𝐫𝐚𝐠𝐞: 𝐂𝐥𝐞𝐚𝐧 𝐨𝐥𝐝 𝐜𝐥𝐨𝐧𝐞𝐬
🐛 𝐁𝐮𝐠𝐬: 𝐑𝐞𝐬𝐭𝐚𝐫𝐭 𝐭𝐡𝐞 𝐛𝐨𝐭

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐒𝐔𝐏𝐏𝐎𝐑𝐓')}

𝐅𝐨𝐫 𝐬𝐮𝐩𝐩𝐨𝐫𝐭, 𝐜𝐨𝐧𝐭𝐚𝐜𝐭:
{Config.SUPPORT_GROUP}
"""
        
        await query.edit_message_text(
            help_text,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("◀️ 𝐁𝐚𝐜𝐤", callback_data="main_menu")]
            ]),
            parse_mode=ParseMode.MARKDOWN
        )
    
    # ==============================================
    # 𝐀𝐃𝐌𝐈𝐍 𝐏𝐀𝐍𝐄𝐋
    # ==============================================
    
    async def show_admin_panel(self, query, user_id: int):
        """Show admin panel"""
        if user_id not in Config.ADMIN_IDS:
            await query.answer("❌ 𝐀𝐜𝐜𝐞𝐬𝐬 𝐝𝐞𝐧𝐢𝐞𝐝!", show_alert=True)
            await self.show_main_menu(query)
            return
        
        admin_text = f"""
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
👑 {EXUFont.bold('𝐀𝐃𝐌𝐈𝐍 𝐂𝐎𝐍𝐓𝐑𝐎𝐋 𝐏𝐀𝐍𝐄𝐋')}
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}

⚡ 𝐖𝐞𝐥𝐜𝐨𝐦𝐞, 𝐀𝐝𝐦𝐢𝐧!

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐀𝐃𝐌𝐈𝐍 𝐓𝐎𝐎𝐋𝐒')}

👥 𝐔𝐬𝐞𝐫 𝐌𝐚𝐧𝐚𝐠𝐞𝐦𝐞𝐧𝐭 - 𝐌𝐚𝐧𝐚𝐠𝐞 𝐮𝐬𝐞𝐫𝐬 & 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧𝐬
📊 𝐁𝐨𝐭 𝐒𝐭𝐚𝐭𝐢𝐬𝐭𝐢𝐜𝐬 - 𝐃𝐞𝐭𝐚𝐢𝐥𝐞𝐝 𝐬𝐭𝐚𝐭𝐬 & 𝐫𝐞𝐩𝐨𝐫𝐭𝐬
⚙️ 𝐁𝐨𝐭 𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬 - 𝐂𝐨𝐧𝐟𝐢𝐠𝐮𝐫𝐞 𝐛𝐨𝐭 𝐬𝐞𝐭𝐭𝐢𝐧𝐠𝐬
📢 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭 - 𝐒𝐞𝐧𝐝 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬 𝐭𝐨 𝐚𝐥𝐥 𝐮𝐬𝐞𝐫𝐬

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒')}

/admin - 𝐎𝐩𝐞𝐧 𝐚𝐝𝐦𝐢𝐧 𝐩𝐚𝐧𝐞𝐥
/stats - 𝐒𝐡𝐨𝐰 𝐝𝐞𝐭𝐚𝐢𝐥𝐞𝐝 𝐬𝐭𝐚𝐭𝐬
/users - 𝐋𝐢𝐬𝐭 𝐚𝐥𝐥 𝐮𝐬𝐞𝐫𝐬
/broadcast - 𝐒𝐞𝐧𝐝 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐭𝐨 𝐚𝐥𝐥
"""
        
        await query.edit_message_text(
            admin_text,
            reply_markup=self.admin_menu(),
            parse_mode=ParseMode.MARKDOWN
        )
    
    async def handle_admin_callback(self, query, context: CallbackContext, data: str, user_id: int):
        """Handle admin panel callbacks"""
        if user_id not in Config.ADMIN_IDS:
            await query.answer("❌ 𝐀𝐜𝐜𝐞𝐬𝐬 𝐝𝐞𝐧𝐢𝐞𝐝!", show_alert=True)
            return
        
        if data == "admin_users":
            await self.show_user_management(query)
        elif data == "admin_stats":
            await self.show_admin_stats(query)
        elif data == "admin_settings":
            await self.show_admin_settings(query)
        elif data == "admin_broadcast":
            await self.start_broadcast(query)
        else:
            await query.answer("⚡ 𝐅𝐞𝐚𝐭𝐮𝐫𝐞 𝐜𝐨𝐦𝐢𝐧𝐠 𝐬𝐨𝐨𝐧!", show_alert=True)
    
    async def show_user_management(self, query):
        """Show user management"""
        cursor = self.db.conn.cursor()
        cursor.execute('SELECT user_id, username, first_name, total_clones, is_banned FROM users ORDER BY last_active DESC LIMIT 20')
        users = cursor.fetchall()
        
        user_list = ""
        for user in users:
            user_id, username, name, clones, banned = user
            status = "⛔" if banned else "✅"
            user_list += f"{status} {name} (@{username or 'N/A'})\n"
            user_list += f"   𝐈𝐃: {user_id} | 𝐂𝐥𝐨𝐧𝐞𝐬: {clones}\n\n"
        
        user_text = f"""
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐔𝐒𝐄𝐑 𝐌𝐀𝐍𝐀𝐆𝐄𝐌𝐄𝐍𝐓')}
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}

{user_list if user_list else "𝐍𝐨 𝐮𝐬𝐞𝐫𝐬 𝐟𝐨𝐮𝐧𝐝."}

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐀𝐃𝐌𝐈𝐍 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒')}

/ban <user_id> - 𝐁𝐚𝐧 𝐮𝐬𝐞𝐫
/unban <user_id> - 𝐔𝐧𝐛𝐚𝐧 𝐮𝐬𝐞𝐫
/users - 𝐋𝐢𝐬𝐭 𝐚𝐥𝐥 𝐮𝐬𝐞𝐫𝐬
/user <user_id> - 𝐕𝐢𝐞𝐰 𝐮𝐬𝐞𝐫 𝐝𝐞𝐭𝐚𝐢𝐥𝐬
"""
        
        await query.edit_message_text(
            user_text,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔄 𝐑𝐞𝐟𝐫𝐞𝐬𝐡", callback_data="admin_users")],
                [InlineKeyboardButton("◀️ 𝐁𝐚𝐜𝐤", callback_data="admin_panel")]
            ]),
            parse_mode=ParseMode.MARKDOWN
        )
    
    async def show_admin_stats(self, query):
        """Show admin statistics"""
        cursor = self.db.conn.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM users')
        total_users = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM clones WHERE status = "success"')
        total_clones = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM users WHERE is_verified = 1')
        verified_users = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM users WHERE is_banned = 1')
        banned_users = cursor.fetchone()[0]
        
        uptime = datetime.now() - self.start_time
        hours, remainder = divmod(int(uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        
        stats_text = f"""
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐀𝐃𝐌𝐈𝐍 𝐒𝐓𝐀𝐓𝐈𝐒𝐓𝐈𝐂𝐒')}
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}

📊 𝐁𝐎𝐓 𝐒𝐓𝐀𝐓𝐒:

• 𝐁𝐨𝐭 𝐔𝐩𝐭𝐢𝐦𝐞: {hours}h {minutes}m {seconds}s
• 𝐌𝐞𝐦𝐨𝐫𝐲 𝐔𝐬𝐚𝐠𝐞: {psutil.Process().memory_info().rss / 1024 / 1024:.1f} MB
• 𝐂𝐏𝐔 𝐔𝐬𝐚𝐠𝐞: {psutil.cpu_percent()}%
• 𝐀𝐜𝐭𝐢𝐯𝐞 𝐂𝐥𝐨𝐧𝐞𝐬: {len(self.active_clones)}

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
👥 𝐔𝐒𝐄𝐑 𝐒𝐓𝐀𝐓𝐒:

• 𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫𝐬: {total_users}
• 𝐕𝐞𝐫𝐢𝐟𝐢𝐞𝐝 𝐔𝐬𝐞𝐫𝐬: {verified_users}
• 𝐁𝐚𝐧𝐧𝐞𝐝 𝐔𝐬𝐞𝐫𝐬: {banned_users}
• 𝐀𝐜𝐭𝐢𝐯𝐞 (𝟐𝟒𝐡): {self.get_active_users_24h()}

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
🚀 𝐂𝐋𝐎𝐍𝐈𝐍𝐆 𝐒𝐓𝐀𝐓𝐒:

• 𝐓𝐨𝐭𝐚𝐥 𝐂𝐥𝐨𝐧𝐞𝐬: {total_clones}
• 𝐓𝐨𝐝𝐚𝐲'𝐬 𝐂𝐥𝐨𝐧𝐞𝐬: {self.get_today_clones()}
• 𝐒𝐮𝐜𝐜𝐞𝐬𝐬 𝐑𝐚𝐭𝐞: {(total_clones / max(total_clones, 1) * 100):.1f}%
"""
        
        await query.edit_message_text(
            stats_text,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔄 𝐑𝐞𝐟𝐫𝐞𝐬𝐡", callback_data="admin_stats")],
                [InlineKeyboardButton("◀️ 𝐁𝐚𝐜𝐤", callback_data="admin_panel")]
            ]),
            parse_mode=ParseMode.MARKDOWN
        )
    
    async def show_admin_settings(self, query):
        """Show admin settings"""
        settings_text = f"""
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐁𝐎𝐓 𝐒𝐄𝐓𝐓𝐈𝐍𝐆𝐒')}
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}

⚙️ 𝐂𝐔𝐑𝐑𝐄𝐍𝐓 𝐒𝐄𝐓𝐓𝐈𝐍𝐆𝐒:

• 𝐂𝐡𝐚𝐧𝐧𝐞𝐥: {Config.CHANNEL_USERNAME}
• 𝐅𝐨𝐫𝐜𝐞 𝐉𝐨𝐢𝐧: {'✅ 𝐎𝐧' if self.db.get_setting('force_join', '1') == '1' else '❌ 𝐎𝐟𝐟'}
• 𝐃𝐚𝐢𝐥𝐲 𝐂𝐥𝐨𝐧𝐞 𝐋𝐢𝐦𝐢𝐭: {self.db.get_setting('max_clones_per_day', '10')}
• 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐌𝐬𝐠: {self.db.get_setting('welcome_msg', 'Welcome')[:30]}...

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐀𝐃𝐌𝐈𝐍 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒')}

/setlimit <number> - 𝐒𝐞𝐭 𝐝𝐚𝐢𝐥𝐲 𝐜𝐥𝐨𝐧𝐞 𝐥𝐢𝐦𝐢𝐭
/toggle_join - 𝐓𝐨𝐠𝐠𝐥𝐞 𝐟𝐨𝐫𝐜𝐞 𝐣𝐨𝐢𝐧
/setwelcome <message> - 𝐒𝐞𝐭 𝐰𝐞𝐥𝐜𝐨𝐦𝐞 𝐦𝐞𝐬𝐬𝐚𝐠𝐞
/setchannel @username - 𝐒𝐞𝐭 𝐜𝐡𝐚𝐧𝐧𝐞𝐥
"""
        
        await query.edit_message_text(
            settings_text,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔄 𝐑𝐞𝐥𝐨𝐚𝐝", callback_data="admin_settings")],
                [InlineKeyboardButton("◀️ 𝐁𝐚𝐜𝐤", callback_data="admin_panel")]
            ]),
            parse_mode=ParseMode.MARKDOWN
        )
    
    async def start_broadcast(self, query):
        """Start broadcast message"""
        broadcast_text = f"""
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐁𝐑𝐎𝐀𝐃𝐂𝐀𝐒𝐓 𝐌𝐄𝐒𝐒𝐀𝐆𝐄')}
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}

📢 𝐒𝐞𝐧𝐝 𝐚 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐭𝐨 𝐚𝐥𝐥 𝐮𝐬𝐞𝐫𝐬:

𝐔𝐬𝐚𝐠𝐞:
/broadcast 𝐘𝐨𝐮𝐫 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐡𝐞𝐫𝐞

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
𝐄𝐱𝐚𝐦𝐩𝐥𝐞:
/broadcast 𝐁𝐨𝐭 𝐰𝐢𝐥𝐥 𝐛𝐞 𝐝𝐨𝐰𝐧 𝐟𝐨𝐫 𝐦𝐚𝐢𝐧𝐭𝐞𝐧𝐚𝐧𝐜𝐞 𝐭𝐨𝐦𝐨𝐫𝐫𝐨𝐰
"""
        
        await query.edit_message_text(
            broadcast_text,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("◀️ 𝐁𝐚𝐜𝐤", callback_data="admin_panel")]
            ]),
            parse_mode=ParseMode.MARKDOWN
        )
    
    # ==============================================
    # 𝐀𝐃𝐌𝐈𝐍 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒
    # ==============================================
    
    async def handle_admin_command(self, update: Update, context: CallbackContext):
        """Handle admin commands"""
        user_id = update.effective_user.id
        
        if user_id not in Config.ADMIN_IDS:
            await update.message.reply_text("❌ 𝐀𝐜𝐜𝐞𝐬𝐬 𝐝𝐞𝐧𝐢𝐞𝐝!")
            return
        
        command = update.message.text.split()[0].lower()
        args = update.message.text.split()[1:] if len(update.message.text.split()) > 1 else []
        
        if command == "/admin":
            await self.show_admin_panel_via_command(update)
        elif command == "/stats":
            await self.send_detailed_stats(update)
        elif command == "/broadcast" and args:
            await self.send_broadcast(update, context, " ".join(args))
        elif command == "/users":
            await self.list_users(update)
        elif command == "/user" and args:
            await self.view_user(update, args[0])
        elif command == "/ban" and args:
            await self.ban_user(update, args[0])
        elif command == "/unban" and args:
            await self.unban_user(update, args[0])
        elif command == "/setlimit" and args:
            await self.set_daily_limit(update, args[0])
        elif command == "/toggle_join":
            await self.toggle_force_join(update)
        elif command == "/setwelcome" and args:
            await self.set_welcome_message(update, " ".join(args))
        elif command == "/setchannel" and args:
            await self.set_channel(update, args[0])
        else:
            await update.message.reply_text(
                f"{EXUFont.bold('📋 𝐀𝐝𝐦𝐢𝐧 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬:')}\n\n"
                "/admin - 𝐎𝐩𝐞𝐧 𝐚𝐝𝐦𝐢𝐧 𝐩𝐚𝐧𝐞𝐥\n"
                "/stats - 𝐃𝐞𝐭𝐚𝐢𝐥𝐞𝐝 𝐬𝐭𝐚𝐭𝐢𝐬𝐭𝐢𝐜𝐬\n"
                "/broadcast <msg> - 𝐒𝐞𝐧𝐝 𝐭𝐨 𝐚𝐥𝐥 𝐮𝐬𝐞𝐫𝐬\n"
                "/users - 𝐋𝐢𝐬𝐭 𝐚𝐥𝐥 𝐮𝐬𝐞𝐫𝐬\n"
                "/user <id> - 𝐕𝐢𝐞𝐰 𝐮𝐬𝐞𝐫 𝐝𝐞𝐭𝐚𝐢𝐥𝐬\n"
                "/ban <id> - 𝐁𝐚𝐧 𝐮𝐬𝐞𝐫\n"
                "/unban <id> - 𝐔𝐧𝐛𝐚𝐧 𝐮𝐬𝐞𝐫\n"
                "/setlimit <num> - 𝐒𝐞𝐭 𝐝𝐚𝐢𝐥𝐲 𝐥𝐢𝐦𝐢𝐭\n"
                "/toggle_join - 𝐓𝐨𝐠𝐠𝐥𝐞 𝐟𝐨𝐫𝐜𝐞 𝐣𝐨𝐢𝐧\n"
                "/setwelcome <msg> - 𝐒𝐞𝐭 𝐰𝐞𝐥𝐜𝐨𝐦𝐞 𝐦𝐞𝐬𝐬𝐚𝐠𝐞\n"
                "/setchannel @user - 𝐒𝐞𝐭 𝐜𝐡𝐚𝐧𝐧𝐞𝐥",
                parse_mode=ParseMode.MARKDOWN
            )
    
    async def show_admin_panel_via_command(self, update: Update):
        """Show admin panel via command"""
        class MockQuery:
            def __init__(self, message, user):
                self.message = message
                self.from_user = user
                self.data = ""
        
        mock_query = MockQuery(update.message, update.effective_user)
        await self.show_admin_panel(mock_query, update.effective_user.id)
    
    async def send_detailed_stats(self, update: Update):
        """Send detailed statistics"""
        cursor = self.db.conn.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM users')
        total_users = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM clones')
        total_clones = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM clones WHERE status = "success"')
        success_clones = cursor.fetchone()[0]
        
        cursor.execute('SELECT SUM(size_mb) FROM clones WHERE status = "success"')
        total_storage = cursor.fetchone()[0] or 0
        
        uptime = datetime.now() - self.start_time
        hours, remainder = divmod(int(uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        
        stats_text = f"""
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐃𝐄𝐓𝐀𝐈𝐋𝐄𝐃 𝐒𝐓𝐀𝐓𝐈𝐒𝐓𝐈𝐂𝐒')}
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}

📅 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

📊 𝐁𝐎𝐓 𝐒𝐓𝐀𝐓𝐒:
• 𝐔𝐩𝐭𝐢𝐦𝐞: {hours}h {minutes}m {seconds}s
• 𝐌𝐞𝐦𝐨𝐫𝐲: {psutil.Process().memory_info().rss / 1024 / 1024:.1f} MB
• 𝐂𝐏𝐔: {psutil.cpu_percent()}%
• 𝐃𝐢𝐬𝐤: {psutil.disk_usage('.').percent}%

👥 𝐔𝐒𝐄𝐑 𝐒𝐓𝐀𝐓𝐒:
• 𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫𝐬: {total_users}
• 𝐕𝐞𝐫𝐢𝐟𝐢𝐞𝐝: {self.db.conn.execute('SELECT COUNT(*) FROM users WHERE is_verified = 1').fetchone()[0]}
• 𝐁𝐚𝐧𝐧𝐞𝐝: {self.db.conn.execute('SELECT COUNT(*) FROM users WHERE is_banned = 1').fetchone()[0]}
• 𝐀𝐜𝐭𝐢𝐯𝐞 (𝟐𝟒𝐡): {self.get_active_users_24h()}

🚀 𝐂𝐋𝐎𝐍𝐄 𝐒𝐓𝐀𝐓𝐒:
• 𝐓𝐨𝐭𝐚𝐥 𝐂𝐥𝐨𝐧𝐞𝐬: {total_clones}
• 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥: {success_clones}
• 𝐒𝐮𝐜𝐜𝐞𝐬𝐬 𝐑𝐚𝐭𝐞: {(success_clones / max(total_clones, 1) * 100):.1f}%
• 𝐓𝐨𝐭𝐚𝐥 𝐒𝐭𝐨𝐫𝐚𝐠𝐞: {total_storage:.2f} MB
• 𝐓𝐨𝐝𝐚𝐲'𝐬 𝐂𝐥𝐨𝐧𝐞𝐬: {self.get_today_clones()}
"""
        
        await update.message.reply_text(stats_text, parse_mode=ParseMode.MARKDOWN)
    
    async def send_broadcast(self, update: Update, context: CallbackContext, message: str):
        """Send broadcast to all users"""
        cursor = self.db.conn.cursor()
        cursor.execute('SELECT user_id FROM users')
        users = cursor.fetchall()
        total = len(users)
        
        broadcast_msg = f"""
📢 {EXUFont.bold('𝐁𝐑𝐎𝐀𝐃𝐂𝐀𝐒𝐓 𝐌𝐄𝐒𝐒𝐀𝐆𝐄')}

{message}

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
- 𝐄𝐗𝐔 𝐂𝐥𝐨𝐧𝐞𝐫 𝐓𝐞𝐚𝐦
"""
        
        status_msg = await update.message.reply_text(f"📤 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭𝐢𝐧𝐠...\n0/{total}")
        
        success = 0
        failed = 0
        
        for i, (user_id,) in enumerate(users, 1):
            try:
                await context.bot.send_message(
                    chat_id=user_id,
                    text=broadcast_msg,
                    parse_mode=ParseMode.MARKDOWN
                )
                success += 1
            except:
                failed += 1
            
            if i % 10 == 0 or i == total:
                await status_msg.edit_text(f"📤 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭𝐢𝐧𝐠...\n{i}/{total}\n✅ {success} | ❌ {failed}")
        
        await status_msg.edit_text(f"📢 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞!\n✅ 𝐒𝐮𝐜𝐜𝐞𝐬𝐬: {success}\n❌ 𝐅𝐚𝐢𝐥𝐞𝐝: {failed}")
    
    async def list_users(self, update: Update):
        """List all users"""
        cursor = self.db.conn.cursor()
        cursor.execute('SELECT user_id, username, first_name, total_clones, is_banned FROM users ORDER BY last_active DESC LIMIT 50')
        users = cursor.fetchall()
        
        user_list = f"📋 {EXUFont.bold('𝐔𝐒𝐄𝐑 𝐋𝐈𝐒𝐓')} ({len(users)}):\n\n"
        for user in users:
            user_id, username, name, clones, banned = user
            status = "⛔" if banned else "✅"
            user_list += f"{status} {name} (@{username or 'N/A'})\n"
            user_list += f"   𝐈𝐃: {user_id} | 𝐂𝐥𝐨𝐧𝐞𝐬: {clones}\n\n"
        
        await update.message.reply_text(user_list[:4000])
    
    async def view_user(self, update: Update, user_id_str: str):
        """View user details"""
        try:
            user_id = int(user_id_str)
            cursor = self.db.conn.cursor()
            cursor.execute('''
                SELECT username, first_name, join_date, last_active, 
                       is_verified, is_banned, total_clones, clones_today
                FROM users WHERE user_id = ?
            ''', (user_id,))
            result = cursor.fetchone()
            
            if not result:
                await update.message.reply_text("❌ 𝐔𝐬𝐞𝐫 𝐧𝐨𝐭 𝐟𝐨𝐮𝐧𝐝.")
                return
            
            username, name, join_date, last_active, verified, banned, total_clones, clones_today = result
            
            user_info = f"""
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐔𝐒𝐄𝐑 𝐃𝐄𝐓𝐀𝐈𝐋𝐒')}
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}

👤 𝐍𝐚𝐦𝐞: {name}
📛 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞: @{username or 'N/A'}
🆔 𝐔𝐬𝐞𝐫 𝐈𝐃: {user_id}
📅 𝐉𝐨𝐢𝐧𝐞𝐝: {join_date}
🕒 𝐋𝐚𝐬𝐭 𝐀𝐜𝐭𝐢𝐯𝐞: {last_active}
🛡️ 𝐒𝐭𝐚𝐭𝐮𝐬: {'✅ 𝐕𝐞𝐫𝐢𝐟𝐢𝐞𝐝' if verified else '⭕ 𝐏𝐞𝐧𝐝𝐢𝐧𝐠'}
🚫 𝐁𝐚𝐧𝐧𝐞𝐝: {'✅ 𝐘𝐞𝐬' if banned else '❌ 𝐍𝐨'}

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
📊 𝐒𝐓𝐀𝐓𝐈𝐒𝐓𝐈𝐂𝐒:

• 𝐓𝐨𝐭𝐚𝐥 𝐂𝐥𝐨𝐧𝐞𝐬: {total_clones}
• 𝐂𝐥𝐨𝐧𝐞𝐬 𝐓𝐨𝐝𝐚𝐲: {clones_today}/{self.db.get_setting('max_clones_per_day', '10')}

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
👑 𝐀𝐃𝐌𝐈𝐍 𝐀𝐂𝐓𝐈𝐎𝐍𝐒:

/ban {user_id} - 𝐁𝐚𝐧 𝐭𝐡𝐢𝐬 𝐮𝐬𝐞𝐫
/unban {user_id} - 𝐔𝐧𝐛𝐚𝐧 𝐭𝐡𝐢𝐬 𝐮𝐬𝐞𝐫
"""
            
            await update.message.reply_text(user_info, parse_mode=ParseMode.MARKDOWN)
            
        except ValueError:
            await update.message.reply_text("❌ 𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐮𝐬𝐞𝐫 𝐈𝐃.")
    
    async def ban_user(self, update: Update, user_id_str: str):
        """Ban user"""
        try:
            user_id = int(user_id_str)
            cursor = self.db.conn.cursor()
            cursor.execute('UPDATE users SET is_banned = 1 WHERE user_id = ?', (user_id,))
            self.db.conn.commit()
            
            await update.message.reply_text(f"✅ 𝐔𝐬𝐞𝐫 {user_id} 𝐡𝐚𝐬 𝐛𝐞𝐞𝐧 𝐛𝐚𝐧𝐧𝐞𝐝.")
            
        except ValueError:
            await update.message.reply_text("❌ 𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐮𝐬𝐞𝐫 𝐈𝐃.")
    
    async def unban_user(self, update: Update, user_id_str: str):
        """Unban user"""
        try:
            user_id = int(user_id_str)
            cursor = self.db.conn.cursor()
            cursor.execute('UPDATE users SET is_banned = 0 WHERE user_id = ?', (user_id,))
            self.db.conn.commit()
            
            await update.message.reply_text(f"✅ 𝐔𝐬𝐞𝐫 {user_id} 𝐡𝐚𝐬 𝐛𝐞𝐞𝐧 𝐮𝐧𝐛𝐚𝐧𝐧𝐞𝐝.")
            
        except ValueError:
            await update.message.reply_text("❌ 𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐮𝐬𝐞𝐫 𝐈𝐃.")
    
    async def set_daily_limit(self, update: Update, limit_str: str):
        """Set daily clone limit"""
        try:
            limit = int(limit_str)
            if limit < 1 or limit > 100:
                raise ValueError
            
            self.db.update_setting('max_clones_per_day', str(limit))
            await update.message.reply_text(f"✅ 𝐃𝐚𝐢𝐥𝐲 𝐜𝐥𝐨𝐧𝐞 𝐥𝐢𝐦𝐢𝐭 𝐬𝐞𝐭 𝐭𝐨: {limit}")
            
        except ValueError:
            await update.message.reply_text("❌ 𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐥𝐢𝐦𝐢𝐭. 𝐏𝐥𝐞𝐚𝐬𝐞 𝐮𝐬𝐞 𝐚 𝐧𝐮𝐦𝐛𝐞𝐫 𝐛𝐞𝐭𝐰𝐞𝐞𝐧 𝟏 𝐚𝐧𝐝 𝟏𝟎𝟎.")
    
    async def toggle_force_join(self, update: Update):
        """Toggle force join"""
        current = self.db.get_setting('force_join', '1')
        new_value = '0' if current == '1' else '1'
        self.db.update_setting('force_join', new_value)
        
        status = "𝐄𝐧𝐚𝐛𝐥𝐞𝐝" if new_value == '1' else "𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝"
        await update.message.reply_text(f"✅ 𝐅𝐨𝐫𝐜𝐞 𝐣𝐨𝐢𝐧 {status}.")
    
    async def set_welcome_message(self, update: Update, message: str):
        """Set welcome message"""
        if len(message) > 200:
            await update.message.reply_text("❌ 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐭𝐨𝐨 𝐥𝐨𝐧𝐠. 𝐌𝐚𝐱 𝟐𝟎𝟎 𝐜𝐡𝐚𝐫𝐚𝐜𝐭𝐞𝐫𝐬.")
            return
        
        self.db.update_setting('welcome_msg', message)
        await update.message.reply_text(f"✅ 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐬𝐞𝐭 𝐭𝐨:\n\n{message}")
    
    async def set_channel(self, update: Update, channel: str):
        """Set channel"""
        if not channel.startswith('@'):
            channel = '@' + channel
        
        # Update configuration
        Config.CHANNEL_USERNAME = channel
        await update.message.reply_text(f"✅ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐬𝐞𝐭 𝐭𝐨: {channel}")
    
    # ==============================================
    # 𝐔𝐓𝐈𝐋𝐈𝐓𝐘 𝐌𝐄𝐓𝐇𝐎𝐃𝐒
    # ==============================================
    
    def get_active_users_24h(self) -> int:
        """Get number of active users in last 24 hours"""
        cursor = self.db.conn.cursor()
        twenty_four_hours_ago = (datetime.now() - timedelta(hours=24)).isoformat()
        cursor.execute('SELECT COUNT(*) FROM users WHERE last_active > ?', (twenty_four_hours_ago,))
        return cursor.fetchone()[0]
    
    def get_today_clones(self) -> int:
        """Get number of clones today"""
        cursor = self.db.conn.cursor()
        today = datetime.now().date().isoformat()
        cursor.execute('SELECT COUNT(*) FROM clones WHERE timestamp LIKE ?', (f'{today}%',))
        return cursor.fetchone()[0]
    
    # ==============================================
    # 𝐁𝐎𝐓 𝐒𝐄𝐓𝐔𝐏 & 𝐑𝐔𝐍
    # ==============================================
    
    async def run(self):
        """Run the bot"""
        # Create application
        self.app = Application.builder().token(Config.TOKEN).build()
        
        # Add command handlers
        self.app.add_handler(CommandHandler("start", self.start_command))
        self.app.add_handler(CommandHandler("help", self.start_command))
        
        # Add admin command handlers
        self.app.add_handler(CommandHandler("admin", self.handle_admin_command))
        self.app.add_handler(CommandHandler("stats", self.handle_admin_command))
        self.app.add_handler(CommandHandler("broadcast", self.handle_admin_command))
        self.app.add_handler(CommandHandler("users", self.handle_admin_command))
        self.app.add_handler(CommandHandler("user", self.handle_admin_command))
        self.app.add_handler(CommandHandler("ban", self.handle_admin_command))
        self.app.add_handler(CommandHandler("unban", self.handle_admin_command))
        self.app.add_handler(CommandHandler("setlimit", self.handle_admin_command))
        self.app.add_handler(CommandHandler("toggle_join", self.handle_admin_command))
        self.app.add_handler(CommandHandler("setwelcome", self.handle_admin_command))
        self.app.add_handler(CommandHandler("setchannel", self.handle_admin_command))
        
        # Add message handler for URLs
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_url_message))
        
        # Add callback handler
        self.app.add_handler(CallbackQueryHandler(self.callback_handler))
        
        # Configure logging
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )
        
        # Start bot
        print(EXUFont.log("🚀", "SYSTEM", "EXU Cloner Bot v4.0 Started"))
        print(EXUFont.log("⚡", "SYSTEM", f"Bot Token: {'*' * len(Config.TOKEN)}"))
        print(EXUFont.log("👑", "ADMIN", f"Admin IDs: {Config.ADMIN_IDS}"))
        print(EXUFont.log("📢", "CHANNEL", f"Channel: {Config.CHANNEL_USERNAME}"))
        print(EXUFont.log("🤖", "SYSTEM", "Bot is now running..."))
        
        await self.app.initialize()
        await self.app.start()
        await self.app.updater.start_polling()
        
        # Keep running
        await asyncio.Event().wait()

# ==============================================
# 𝐌𝐀𝐈𝐍 𝐄𝐗𝐄𝐂𝐔𝐓𝐈𝐎𝐍
# ==============================================

async def main():
    """Main execution function"""
    try:
        bot = EXUClonerBot()
        await bot.run()
    except KeyboardInterrupt:
        print("\n" + EXUFont.log("⚠️", "SYSTEM", "Bot shutdown requested"))
    except Exception as e:
        print(EXUFont.log("❌", "SYSTEM", f"Fatal error: {str(e)}"))
        import traceback
        traceback.print_exc()
    finally:
        print(EXUFont.log("🤖", "SYSTEM", "EXU Cloner Bot stopped"))

if __name__ == "__main__":
    asyncio.run(main())
