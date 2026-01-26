#!/usr/bin/env python3
"""
ＥＸＵ ＣＬＯＮＥＲ ＳＵＰＲＥＭＥ ＰＲＯ
Ultimate Website Cloner Telegram Bot with Advanced Features
Builder: EXU Coder Supreme Edition
"""

import os
import sys
import asyncio
import logging
import tempfile
import shutil
import zipfile
import tarfile
import random
import re
import json
import sqlite3
import time
import hashlib
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
import html
import base64
from io import BytesIO

# Enhanced Auto-install dependencies
def install_deps():
    print("\n" + "="*60)
    print("𝐈𝐍𝐒𝐓𝐀𝐋𝐋𝐈𝐍𝐆 𝐀𝐃𝐕𝐀𝐍𝐂𝐄𝐃 𝐃𝐄𝐏𝐄𝐍𝐃𝐄𝐍𝐂𝐈𝐄𝐒...")
    print("="*60)
    
    deps = [
        "python-telegram-bot==20.7",
        "beautifulsoup4==4.12.2",
        "requests==2.31.0",
        "aiohttp==3.9.1",
        "aiofiles==23.2.1",
        "Pillow==10.1.0",
        "psutil==5.9.6",
        "qrcode==7.4.2",
        "cloudscraper==1.2.71",
        "cssutils==2.7.1",
        "tqdm==4.66.1"
    ]
    
    import subprocess
    for dep in deps:
        print(f"📦 {dep}")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep, "-q"])
            print(f"   ✅ Installed")
        except:
            print(f"   ❌ Failed")
    
    print("="*60)
    print(f"✅ 𝐀𝐃𝐕𝐀𝐍𝐂𝐄𝐃 𝐃𝐄𝐏𝐄𝐍𝐃𝐄𝐍𝐂𝐈𝐄𝐒 𝐈𝐍𝐒𝐓𝐀𝐋𝐋𝐄𝐃")
    print("="*60 + "\n")

try:
    from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
    from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler
    from telegram.constants import ParseMode
    
    import aiohttp
    from bs4 import BeautifulSoup
    import requests
    from PIL import Image, ImageDraw, ImageFont, ImageFilter
    import qrcode
    import psutil
    import cloudscraper
    import cssutils
    from tqdm import tqdm
except ImportError:
    install_deps()
    from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
    from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler
    from telegram.constants import ParseMode
    
    import aiohttp
    from bs4 import BeautifulSoup
    import requests
    from PIL import Image, ImageDraw, ImageFont, ImageFilter
    import qrcode
    import psutil
    import cloudscraper
    import cssutils
    from tqdm import tqdm

# ==============================================
# 𝐄𝐗𝐔 𝐅𝐎𝐍𝐓 𝐒𝐓𝐘𝐋𝐄𝐒 𝐏𝐑𝐎
# ==============================================

class EXUFont:
    """EXU Font Styling System Pro"""
    
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
    def create_progress(progress: float, length: int = 20, style: str = "cyber") -> str:
        """Create advanced progress bar with EXU style"""
        filled = int(progress * length)
        empty = length - filled
        
        if style == "cyber":
            bars = "█" * filled + "░" * empty
        elif style == "dots":
            bars = "⣿" * filled + "⣀" * empty
        elif style == "blocks":
            bars = "🟧" * filled + "⬜" * empty
        else:
            bars = "▰" * filled + "▱" * empty
        
        percent = int(progress * 100)
        
        animations = ["⚡", "🌀", "💫", "✨", "🌟", "🔥"]
        animation = random.choice(animations) if progress < 1.0 else "✅"
        
        if progress < 1.0:
            return f"{animation} {EXUFont.bold('𝐄𝐗𝐄𝐂𝐔𝐓𝐈𝐍𝐆:')} [{bars}] {percent}%"
        else:
            return f"✅ {EXUFont.bold('𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄:')} [{bars}] {percent}%"
    
    @staticmethod
    def banner() -> str:
        """Create EXU PRO banner"""
        return """
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                        ┃
┃      ███████╗██╗  ██╗██╗   ██╗    ██████╗ ██████╗     ┃
┃      ██╔════╝╚██╗██╔╝██║   ██║   ██╔════╝██╔═══██╗    ┃
┃      █████╗   ╚███╔╝ ██║   ██║   ██║     ██║   ██╗    ┃
┃      ██╔══╝   ██╔██╗ ██║   ██║   ██║     ██║   ██║    ┃
┃      ███████╗██╔╝ ██╗╚██████╔╝██╗╚██████╗╚██████╔╝    ┃
┃      ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝ ╚═════╝ ╚═════╝     ┃
┃                                                        ┃
┃               𝐂𝐘𝐁𝐄𝐑 𝐂𝐋𝐎𝐍𝐄𝐑 𝐏𝐑𝐎 𝐕6.0                  ┃
┃               𝐁𝐮𝐢𝐥𝐝𝐞𝐫: 𝐄𝐗𝐔 𝐂𝐨𝐝𝐞𝐫 𝐏𝐑𝐎                 ┃
┃                                                        ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""
    
    @staticmethod
    def header(text: str, style: str = "double") -> str:
        """Create advanced header"""
        if style == "double":
            line = "═" * 50
        elif style == "star":
            line = "★" * 25
        elif style == "dash":
            line = "─" * 50
        else:
            line = "━" * 50
        
        return f"\n{EXUFont.bold(line)}\n{EXUFont.bold(text.center(50))}\n{EXUFont.bold(line)}"
    
    @staticmethod
    def log(icon: str, module: str, message: str, level: str = "INFO") -> str:
        """Create advanced log message"""
        time_str = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        
        level_colors = {
            "INFO": "📘",
            "SUCCESS": "📗",
            "WARNING": "📒",
            "ERROR": "📕",
            "DEBUG": "📓"
        }
        
        level_icon = level_colors.get(level, "📄")
        
        return f"{icon} {level_icon} [{time_str}] [{EXUFont.bold(module)}]: {message}"

# ==============================================
# 𝐀𝐃𝐕𝐀𝐍𝐂𝐄𝐃 𝐂𝐎𝐍𝐅𝐈𝐆𝐔𝐑𝐀𝐓𝐈𝐎𝐍 𝐒𝐘𝐒𝐓𝐄𝐌
# ==============================================

class Config:
    """Advanced Configuration System"""
    
    # Bot Configuration
    TOKEN = "8398989143:AAHZWQUM0h1vHqqOCNWxh8_5bT1FbelOeoQ"
    ADMIN_IDS = [8469461108]
    CHANNEL_USERNAME = "@exucoder1"
    SUPPORT_GROUP = "@exulive"
    BOT_USERNAME = "@EXUClonerBot"
    
    # Web Configuration
    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1"
    ]
    
    # Cloning Configuration
    MAX_CLONE_SIZE_MB = 100
    MAX_CLONES_PER_DAY = 20
    MAX_PAGES_PER_CLONE = 10
    MAX_DEPTH = 2
    CLEANUP_MINUTES = 10
    CACHE_DURATION_HOURS = 24
    
    # Performance
    MAX_CONCURRENT_CLONES = 3
    REQUEST_TIMEOUT = 30
    
    # Output Formats
    OUTPUT_FORMATS = ["zip", "tar.gz", "single_html", "git"]
    DEFAULT_FORMAT = "zip"

# ==============================================
# 𝐀𝐃𝐕𝐀𝐍𝐂𝐄𝐃 𝐃𝐀𝐓𝐀𝐁𝐀𝐒𝐄 𝐒𝐘𝐒𝐓𝐄𝐌
# ==============================================

class AdvancedDatabase:
    """Enhanced Database System with Caching"""
    
    def __init__(self):
        self.conn = sqlite3.connect('exu_cloner_pro.db', check_same_thread=False)
        self.cache = {}
        self.init_db()
    
    def init_db(self):
        cursor = self.conn.cursor()
        
        # Enhanced Users table
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
                last_clone_date TEXT,
                settings_json TEXT DEFAULT '{}',
                bookmarks_json TEXT DEFAULT '[]',
                credits INTEGER DEFAULT 100,
                level INTEGER DEFAULT 1,
                xp INTEGER DEFAULT 0
            )
        ''')
        
        # Enhanced Clones table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                url TEXT,
                title TEXT,
                size_mb REAL,
                status TEXT,
                format TEXT,
                pages INTEGER DEFAULT 1,
                depth INTEGER DEFAULT 1,
                resources_found INTEGER DEFAULT 0,
                resources_downloaded INTEGER DEFAULT 0,
                quality_score INTEGER DEFAULT 0,
                timestamp TEXT,
                metadata_json TEXT DEFAULT '{}'
            )
        ''')
        
        # Settings table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value TEXT,
                category TEXT DEFAULT 'general',
                description TEXT
            )
        ''')
        
        # Queue table for batch processing
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS queue (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                urls_json TEXT,
                status TEXT DEFAULT 'pending',
                progress INTEGER DEFAULT 0,
                created_at TEXT,
                completed_at TEXT
            )
        ''')
        
        # Insert default settings
        defaults = [
            ('force_join', '1', 'security', 'Force users to join channel'),
            ('welcome_msg', '𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐄𝐗𝐔 𝐂𝐥𝐨𝐧𝐞𝐫 𝐏𝐑𝐎!', 'messages', 'Welcome message'),
            ('max_clones_per_day', '20', 'limits', 'Maximum clones per day per user'),
            ('max_clone_size', '100', 'limits', 'Maximum clone size in MB'),
            ('default_format', 'zip', 'output', 'Default output format'),
            ('enable_cache', '1', 'performance', 'Enable caching'),
            ('enable_preview', '1', 'features', 'Enable website preview'),
            ('language', 'en', 'general', 'Default language')
        ]
        
        cursor.executemany(
            'INSERT OR IGNORE INTO settings (key, value, category, description) VALUES (?, ?, ?, ?)',
            defaults
        )
        
        self.conn.commit()
        print(EXUFont.log("💾", "DATABASE", "Advanced database initialized", "SUCCESS"))
    
    def get_setting(self, key: str, default: str = "") -> str:
        """Get setting with caching"""
        cache_key = f"setting_{key}"
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        cursor = self.conn.cursor()
        cursor.execute('SELECT value FROM settings WHERE key = ?', (key,))
        result = cursor.fetchone()
        
        value = result[0] if result else default
        self.cache[cache_key] = value
        return value
    
    def update_setting(self, key: str, value: str):
        """Update setting with cache invalidation"""
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)
        ''', (key, value))
        self.conn.commit()
        
        # Invalidate cache
        cache_key = f"setting_{key}"
        if cache_key in self.cache:
            del self.cache[cache_key]
    
    def add_user(self, user_id: int, username: str, first_name: str):
        """Add or update user with advanced features"""
        cursor = self.conn.cursor()
        
        # Check if user exists
        cursor.execute('SELECT user_id FROM users WHERE user_id = ?', (user_id,))
        exists = cursor.fetchone()
        
        if not exists:
            # New user with default settings
            default_settings = {
                'theme': 'dark',
                'notifications': True,
                'auto_download': True,
                'quality': 'high',
                'format': self.get_setting('default_format', 'zip')
            }
            
            cursor.execute('''
                INSERT INTO users 
                (user_id, username, first_name, join_date, last_active, settings_json)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                user_id, 
                username or "", 
                first_name or "", 
                datetime.now().isoformat(), 
                datetime.now().isoformat(),
                json.dumps(default_settings)
            ))
            print(EXUFont.log("👤", "DATABASE", f"New user added: {user_id}", "SUCCESS"))
        else:
            # Update existing user
            cursor.execute('''
                UPDATE users SET 
                username = ?,
                first_name = ?,
                last_active = ?
                WHERE user_id = ?
            ''', (username or "", first_name or "", datetime.now().isoformat(), user_id))
        
        self.conn.commit()
    
    def get_user_settings(self, user_id: int) -> Dict:
        """Get user settings"""
        cursor = self.conn.cursor()
        cursor.execute('SELECT settings_json FROM users WHERE user_id = ?', (user_id,))
        result = cursor.fetchone()
        
        if result and result[0]:
            return json.loads(result[0])
        return {}
    
    def update_user_settings(self, user_id: int, settings: Dict):
        """Update user settings"""
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE users SET settings_json = ? WHERE user_id = ?
        ''', (json.dumps(settings), user_id))
        self.conn.commit()
    
    def add_bookmark(self, user_id: int, url: str, title: str):
        """Add bookmark for user"""
        cursor = self.conn.cursor()
        cursor.execute('SELECT bookmarks_json FROM users WHERE user_id = ?', (user_id,))
        result = cursor.fetchone()
        
        bookmarks = []
        if result and result[0]:
            bookmarks = json.loads(result[0])
        
        # Check if already bookmarked
        for bookmark in bookmarks:
            if bookmark.get('url') == url:
                return False
        
        bookmarks.append({
            'url': url,
            'title': title[:100],
            'added': datetime.now().isoformat()
        })
        
        cursor.execute('''
            UPDATE users SET bookmarks_json = ? WHERE user_id = ?
        ''', (json.dumps(bookmarks), user_id))
        self.conn.commit()
        return True
    
    def get_bookmarks(self, user_id: int) -> List[Dict]:
        """Get user bookmarks"""
        cursor = self.conn.cursor()
        cursor.execute('SELECT bookmarks_json FROM users WHERE user_id = ?', (user_id,))
        result = cursor.fetchone()
        
        if result and result[0]:
            return json.loads(result[0])
        return []
    
    def record_clone_advanced(self, user_id: int, data: Dict):
        """Record clone with advanced analytics"""
        cursor = self.conn.cursor()
        
        # Update user stats
        cursor.execute('''
            UPDATE users SET 
                total_clones = total_clones + 1,
                clones_today = clones_today + 1,
                last_clone_date = ?,
                xp = xp + ?
            WHERE user_id = ?
        ''', (datetime.now().isoformat(), data.get('xp', 10), user_id))
        
        # Record clone
        cursor.execute('''
            INSERT INTO clones (
                user_id, url, title, size_mb, status, format,
                pages, depth, resources_found, resources_downloaded,
                quality_score, timestamp, metadata_json
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            user_id,
            data.get('url', ''),
            data.get('title', 'Unknown'),
            data.get('file_size', 0),
            data.get('status', 'unknown'),
            data.get('format', 'zip'),
            data.get('pages', 1),
            data.get('depth', 1),
            data.get('resources_found', 0),
            data.get('resources_downloaded', 0),
            data.get('quality_score', 0),
            datetime.now().isoformat(),
            json.dumps(data.get('metadata', {}))
        ))
        
        self.conn.commit()
    
    def add_to_queue(self, user_id: int, urls: List[str]) -> int:
        """Add URLs to batch queue"""
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO queue (user_id, urls_json, created_at)
            VALUES (?, ?, ?)
        ''', (user_id, json.dumps(urls), datetime.now().isoformat()))
        
        self.conn.commit()
        return cursor.lastrowid
    
    def get_queue_status(self, queue_id: int) -> Dict:
        """Get queue status"""
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT user_id, urls_json, status, progress, created_at, completed_at
            FROM queue WHERE id = ?
        ''', (queue_id,))
        result = cursor.fetchone()
        
        if result:
            return {
                'user_id': result[0],
                'urls': json.loads(result[1]),
                'status': result[2],
                'progress': result[3],
                'created_at': result[4],
                'completed_at': result[5]
            }
        return {}
    
    def get_user_stats_advanced(self, user_id: int) -> Dict:
        """Get advanced user statistics"""
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT 
                username, first_name, total_clones, clones_today, 
                join_date, credits, level, xp,
                (SELECT COUNT(*) FROM clones WHERE user_id = ? AND status = 'success') as success_count,
                (SELECT AVG(quality_score) FROM clones WHERE user_id = ? AND status = 'success') as avg_quality,
                (SELECT SUM(size_mb) FROM clones WHERE user_id = ? AND status = 'success') as total_storage
            FROM users WHERE user_id = ?
        ''', (user_id, user_id, user_id, user_id))
        result = cursor.fetchone()
        
        if result:
            return {
                'username': result[0],
                'name': result[1],
                'total_clones': result[2] or 0,
                'clones_today': result[3] or 0,
                'join_date': result[4],
                'credits': result[5] or 100,
                'level': result[6] or 1,
                'xp': result[7] or 0,
                'success_count': result[8] or 0,
                'avg_quality': float(result[9] or 0),
                'total_storage': float(result[10] or 0),
                'success_rate': ((result[8] or 0) / max(result[2] or 1, 1)) * 100
            }
        return {}
    
    def is_verified(self, user_id: int) -> bool:
        """Check if user is verified"""
        cursor = self.conn.cursor()
        cursor.execute('SELECT is_verified FROM users WHERE user_id = ?', (user_id,))
        result = cursor.fetchone()
        return result and result[0] == 1
    
    def is_banned(self, user_id: int) -> bool:
        """Check if user is banned"""
        cursor = self.conn.cursor()
        cursor.execute('SELECT is_banned FROM users WHERE user_id = ?', (user_id,))
        result = cursor.fetchone()
        return result and result[0] == 1
    
    def can_clone_today(self, user_id: int) -> bool:
        """Check if user can clone today"""
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
        
        max_clones = int(self.get_setting('max_clones_per_day', '20'))
        return clones_today < max_clones
    
    def verify_user(self, user_id: int):
        """Verify user"""
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE users SET is_verified = 1 WHERE user_id = ?
        ''', (user_id,))
        self.conn.commit()
    
    def update_activity(self, user_id: int):
        """Update user last activity"""
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE users SET last_active = ? WHERE user_id = ?
        ''', (datetime.now().isoformat(), user_id))
        self.conn.commit()

# ==============================================
# 𝐀𝐃𝐕𝐀𝐍𝐂𝐄𝐃 𝐀𝐍𝐈𝐌𝐀𝐓𝐈𝐎𝐍 𝐄𝐍𝐆𝐈𝐍𝐄
# ==============================================

class AdvancedAnimationEngine:
    """EXU Advanced Animation System"""
    
    @staticmethod
    async def progress_animation(message, text: str, duration: float = 3.0, 
                                 steps: int = 20, style: str = "cyber"):
        """Show advanced progress animation"""
        stages = [
            "𝐈𝐧𝐢𝐭𝐢𝐚𝐥𝐢𝐳𝐢𝐧𝐠 𝐂𝐲𝐛𝐞𝐫 𝐒𝐲𝐬𝐭𝐞𝐦...",
            "𝐀𝐧𝐚𝐥𝐲𝐳𝐢𝐧𝐠 𝐖𝐞𝐛𝐬𝐢𝐭𝐞 𝐒𝐭𝐫𝐮𝐜𝐭𝐮𝐫𝐞...",
            "𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐀𝐬𝐬𝐞𝐭𝐬...",
            "𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐇𝐓𝐌𝐋 & 𝐂𝐒𝐒...",
            "𝐎𝐩𝐭𝐢𝐦𝐢𝐳𝐢𝐧𝐠 𝐑𝐞𝐬𝐨𝐮𝐫𝐜𝐞𝐬...",
            "𝐂𝐫𝐞𝐚𝐭𝐢𝐧𝐠 𝐎𝐮𝐭𝐩𝐮𝐭 𝐏𝐚𝐜𝐤𝐚𝐠𝐞...",
            "𝐕𝐞𝐫𝐢𝐟𝐲𝐢𝐧𝐠 𝐈𝐧𝐭𝐞𝐠𝐫𝐢𝐭𝐲...",
            "𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐏𝐫𝐞𝐯𝐢𝐞𝐰...",
            "𝐅𝐢𝐧𝐚𝐥𝐢𝐳𝐢𝐧𝐠 𝐂𝐥𝐨𝐧𝐞..."
        ]
        
        for i in range(steps + 1):
            progress = i / steps
            stage_idx = min(int(progress * len(stages)), len(stages) - 1)
            
            bar = EXUFont.create_progress(progress, 20, style)
            stage = stages[stage_idx]
            
            update_text = f"""
{EXUFont.bold('━' * 50)}
{EXUFont.bold('𝐄𝐗𝐔 𝐂𝐋𝐎𝐍𝐄𝐑 𝐏𝐑𝐎 - 𝐂𝐘𝐁𝐄𝐑 𝐌𝐎𝐃𝐄')}
{EXUFont.bold('━' * 50)}

{bar}

{EXUFont.bold('📊 𝐒𝐭𝐚𝐠𝐞:')} {stage}
{EXUFont.bold('💾 𝐓𝐚𝐬𝐤:')} {text}

{EXUFont.bold('━' * 50)}
⚡ {EXUFont.bold('𝐒𝐭𝐚𝐭𝐮𝐬:')} {'𝐀𝐜𝐭𝐢𝐯𝐞' if progress < 1.0 else '𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞'}
"""
            try:
                await message.edit_text(update_text, parse_mode=ParseMode.MARKDOWN)
            except:
                pass
            
            await asyncio.sleep(duration / steps)
    
    @staticmethod
    def generate_qr_code(data: str, size: int = 10) -> BytesIO:
        """Generate QR code with EXU style"""
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=size,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="#00ff00", back_color="#000000")
        
        # Convert to BytesIO
        img_bytes = BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        
        return img_bytes
    
    @staticmethod
    def create_preview_image(url: str, title: str = "") -> BytesIO:
        """Create website preview image"""
        # Create a simple preview image
        img = Image.new('RGB', (800, 400), color=(13, 17, 23))
        draw = ImageDraw.Draw(img)
        
        # Add EXU branding
        try:
            font_large = ImageFont.truetype("arial.ttf", 32)
            font_medium = ImageFont.truetype("arial.ttf", 20)
            font_small = ImageFont.truetype("arial.ttf", 16)
        except:
            font_large = ImageFont.load_default()
            font_medium = ImageFont.load_default()
            font_small = ImageFont.load_default()
        
        # Draw title
        draw.text((50, 50), "EXU CLONER PRO", fill=(0, 255, 0), font=font_large)
        draw.text((50, 100), "Website Preview", fill=(200, 200, 200), font=font_medium)
        
        # Draw URL box
        draw.rectangle([50, 150, 750, 200], outline=(0, 255, 0), width=2)
        draw.text((60, 160), f"URL: {url[:60]}", fill=(255, 255, 255), font=font_small)
        
        # Draw title box
        if title:
            draw.rectangle([50, 220, 750, 270], outline=(0, 150, 255), width=2)
            draw.text((60, 230), f"Title: {title[:60]}", fill=(255, 255, 255), font=font_small)
        
        # Draw EXU logo
        draw.rectangle([50, 300, 100, 350], fill=(0, 255, 0))
        draw.text((55, 305), "EXU", fill=(0, 0, 0), font=font_small)
        
        # Convert to BytesIO
        img_bytes = BytesIO()
        img.save(img_bytes, format='PNG', quality=95)
        img_bytes.seek(0)
        
        return img_bytes

# ==============================================
# 𝐀𝐃𝐕𝐀𝐍𝐂𝐄𝐃 𝐖𝐄𝐁𝐒𝐈𝐓𝐄 𝐂𝐋𝐎𝐍𝐄𝐑
# ==============================================

class AdvancedWebsiteCloner:
    """Enhanced Website Cloner with Multiple Features"""
    
    def __init__(self):
        self.temp_dir = None
        self.session = None
        self.scraper = None
        self.stats = {
            'pages_cloned': 0,
            'resources_found': 0,
            'resources_downloaded': 0,
            'total_size': 0,
            'start_time': None,
            'end_time': None
        }
    
    async def initialize(self):
        """Initialize advanced cloner"""
        self.temp_dir = tempfile.mkdtemp(prefix="exu_pro_clone_")
        self.session = aiohttp.ClientSession()
        self.scraper = cloudscraper.create_scraper()
        self.stats['start_time'] = datetime.now()
        
        print(EXUFont.log("🚀", "CLONER", "Advanced cloner initialized", "SUCCESS"))
        return self
    
    async def clone_website_advanced(self, url: str, options: Dict = None) -> Dict:
        """Clone website with advanced options"""
        options = options or {}
        
        try:
            # Validate URL
            if not self.validate_url(url):
                return {
                    'success': False,
                    'error': 'Invalid URL format',
                    'quality_score': 0
                }
            
            # Determine cloning strategy
            strategy = self.determine_cloning_strategy(url, options)
            
            # Execute cloning based on strategy
            if strategy == 'deep':
                result = await self.deep_clone(url, options)
            elif strategy == 'smart':
                result = await self.smart_clone(url, options)
            else:
                result = await self.basic_clone(url, options)
            
            # Calculate quality score
            result['quality_score'] = self.calculate_quality_score(result)
            
            return result
            
        except Exception as e:
            error_msg = str(e)
            print(EXUFont.log("❌", "CLONER", f"Clone failed: {error_msg}", "ERROR"))
            
            return {
                'success': False,
                'error': error_msg,
                'quality_score': 0
            }
    
    async def deep_clone(self, url: str, options: Dict) -> Dict:
        """Deep clone with multiple pages"""
        max_pages = options.get('max_pages', Config.MAX_PAGES_PER_CLONE)
        max_depth = options.get('max_depth', Config.MAX_DEPTH)
        
        print(EXUFont.log("🔍", "CLONER", f"Starting deep clone: {url}", "INFO"))
        
        all_pages = []
        visited = set()
        to_visit = [(url, 1)]  # (url, depth)
        
        while to_visit and len(all_pages) < max_pages:
            current_url, depth = to_visit.pop(0)
            
            if current_url in visited or depth > max_depth:
                continue
            
            visited.add(current_url)
            
            try:
                # Clone current page
                page_result = await self.basic_clone(current_url, options)
                
                if page_result.get('success'):
                    all_pages.append({
                        'url': current_url,
                        'title': page_result.get('title', 'Untitled'),
                        'content': page_result.get('html_content', ''),
                        'resources': page_result.get('resources', [])
                    })
                    
                    # Extract internal links for further cloning
                    if depth < max_depth:
                        internal_links = self.extract_internal_links(
                            page_result.get('html_content', ''), 
                            url
                        )
                        
                        for link in internal_links:
                            if link not in visited:
                                to_visit.append((link, depth + 1))
                
            except Exception as e:
                print(EXUFont.log("⚠️", "CLONER", f"Failed to clone {current_url}: {str(e)}", "WARNING"))
        
        # Create multi-page package
        return await self.create_multi_page_package(all_pages, url, options)
    
    async def smart_clone(self, url: str, options: Dict) -> Dict:
        """Smart cloning with auto-detection"""
        try:
            # Analyze website type
            website_type = await self.analyze_website_type(url)
            
            print(EXUFont.log("🤖", "CLONER", f"Smart clone detected: {website_type}", "INFO"))
            
            # Apply appropriate strategy based on type
            if website_type == 'static':
                return await self.basic_clone(url, options)
            elif website_type == 'multi_page':
                return await self.deep_clone(url, options)
            else:
                return await self.basic_clone(url, options)
                
        except Exception as e:
            print(EXUFont.log("⚠️", "CLONER", f"Smart clone failed: {str(e)}", "WARNING"))
            return await self.basic_clone(url, options)
    
    async def basic_clone(self, url: str, options: Dict) -> Dict:
        """Basic website cloning"""
        try:
            headers = {'User-Agent': random.choice(Config.USER_AGENTS)}
            
            async with self.session.get(url, headers=headers, timeout=Config.REQUEST_TIMEOUT) as response:
                html_content = await response.text()
            
            # Parse HTML
            soup = BeautifulSoup(html_content, 'html.parser')
            title = soup.title.string if soup.title else "Website Clone"
            
            # Extract resources
            resources = self.extract_resources(soup, url)
            
            # Create package
            result = await self.create_package(
                soup, 
                resources, 
                url, 
                title, 
                options.get('format', Config.DEFAULT_FORMAT)
            )
            
            result['strategy'] = 'basic'
            return result
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'strategy': 'basic'
            }
    
    def extract_resources(self, soup: BeautifulSoup, base_url: str) -> List[Tuple[str, str]]:
        """Extract all resources from HTML"""
        resources = []
        
        # CSS files
        for link in soup.find_all('link', rel='stylesheet'):
            href = link.get('href')
            if href:
                resources.append(('css', self.normalize_url(href, base_url)))
        
        # JS files
        for script in soup.find_all('script', src=True):
            src = script.get('src')
            if src:
                resources.append(('js', self.normalize_url(src, base_url)))
        
        # Images
        for img in soup.find_all('img', src=True):
            src = img.get('src')
            if src:
                resources.append(('img', self.normalize_url(src, base_url)))
        
        # Background images in CSS
        for tag in soup.find_all(style=True):
            style = tag['style']
            urls = re.findall(r'url\((.*?)\)', style)
            for url in urls:
                url = url.strip('"\'').strip()
                if url.startswith(('http://', 'https://', '//', '/')):
                    resources.append(('css_img', self.normalize_url(url, base_url)))
        
        # Fonts
        for link in soup.find_all('link', rel=['preload', 'stylesheet']):
            href = link.get('href')
            if href and any(ext in href for ext in ['.woff', '.woff2', '.ttf', '.eot', '.otf']):
                resources.append(('font', self.normalize_url(href, base_url)))
        
        return resources
    
    def normalize_url(self, url: str, base_url: str) -> str:
        """Normalize URL to absolute URL"""
        if url.startswith('//'):
            return 'https:' + url
        elif url.startswith('/'):
            # Get base domain
            from urllib.parse import urlparse
            parsed = urlparse(base_url)
            return f"{parsed.scheme}://{parsed.netloc}{url}"
        elif not url.startswith(('http://', 'https://')):
            return base_url.rstrip('/') + '/' + url.lstrip('/')
        return url
    
    async def download_resource(self, url: str, resource_type: str) -> Optional[bytes]:
        """Download resource with error handling"""
        try:
            headers = {'User-Agent': random.choice(Config.USER_AGENTS)}
            
            async with self.session.get(url, headers=headers, timeout=10) as response:
                if response.status == 200:
                    content = await response.read()
                    
                    # Validate content based on type
                    if self.validate_resource(content, resource_type):
                        return content
                    else:
                        print(EXUFont.log("⚠️", "CLONER", f"Invalid resource: {url}", "WARNING"))
                        return None
                else:
                    print(EXUFont.log("⚠️", "CLONER", f"Failed to download: {url} ({response.status})", "WARNING"))
                    return None
                    
        except Exception as e:
            print(EXUFont.log("⚠️", "CLONER", f"Download error for {url}: {str(e)}", "WARNING"))
            return None
    
    def validate_resource(self, content: bytes, resource_type: str) -> bool:
        """Validate downloaded resource"""
        if not content:
            return False
        
        # Basic validation
        if resource_type == 'img':
            # Check if it's a valid image
            try:
                Image.open(BytesIO(content)).verify()
                return True
            except:
                return False
        
        elif resource_type in ['css', 'js']:
            # Check minimum size for CSS/JS
            return len(content) > 10
        
        return True
    
    async def create_package(self, soup: BeautifulSoup, resources: List[Tuple[str, str]], 
                           url: str, title: str, output_format: str) -> Dict:
        """Create output package in specified format"""
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
        resource_map = {}
        
        for i, (rtype, resource_url) in enumerate(tqdm(resources[:50], desc="Downloading resources")):
            try:
                content = await self.download_resource(resource_url, rtype)
                if content:
                    # Determine file extension
                    ext = self.get_file_extension(resource_url, rtype)
                    filename = f"{rtype}_{i:03d}.{ext}"
                    filepath = os.path.join(assets_dir, filename)
                    
                    with open(filepath, 'wb') as f:
                        f.write(content)
                    
                    # Update HTML to use local resources
                    resource_map[resource_url] = f"assets/{filename}"
                    downloaded += 1
                    
                    # Update stats
                    self.stats['resources_downloaded'] += 1
                    self.stats['total_size'] += len(content)
            except Exception as e:
                continue
        
        # Update HTML with local resource paths
        self.update_html_resources(html_file, resource_map)
        
        # Create output based on format
        output_path = None
        file_size = 0
        
        if output_format == 'zip':
            output_path = await self.create_zip_package(package_dir, title)
        elif output_format == 'tar.gz':
            output_path = await self.create_tar_package(package_dir, title)
        elif output_format == 'single_html':
            output_path = await self.create_single_html(package_dir, title)
        
        if output_path and os.path.exists(output_path):
            file_size = os.path.getsize(output_path) / (1024 * 1024)
        
        self.stats['end_time'] = datetime.now()
        self.stats['pages_cloned'] = 1
        self.stats['resources_found'] = len(resources)
        
        return {
            'success': True,
            'title': title,
            'output_path': output_path,
            'file_size': file_size,
            'resources_found': len(resources),
            'resources_downloaded': downloaded,
            'format': output_format,
            'strategy': 'package',
            'html_content': str(soup),
            'resources': resources,
            'metadata': {
                'clone_time': (self.stats['end_time'] - self.stats['start_time']).total_seconds(),
                'compression_ratio': downloaded / max(len(resources), 1),
                'avg_resource_size': self.stats['total_size'] / max(downloaded, 1) if downloaded > 0 else 0
            }
        }
    
    async def create_zip_package(self, source_dir: str, title: str) -> str:
        """Create ZIP package"""
        output_path = os.path.join(self.temp_dir, f"{self.slugify(title)}_clone.zip")
        
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, source_dir)
                    zipf.write(file_path, arcname)
        
        return output_path
    
    async def create_tar_package(self, source_dir: str, title: str) -> str:
        """Create TAR.GZ package"""
        output_path = os.path.join(self.temp_dir, f"{self.slugify(title)}_clone.tar.gz")
        
        with tarfile.open(output_path, 'w:gz') as tar:
            tar.add(source_dir, arcname=os.path.basename(source_dir))
        
        return output_path
    
    async def create_single_html(self, source_dir: str, title: str) -> str:
        """Create single HTML file with embedded resources"""
        html_file = os.path.join(source_dir, "index.html")
        
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Embed CSS
        css_files = []
        for file in os.listdir(os.path.join(source_dir, "assets")):
            if file.endswith('.css'):
                css_files.append(file)
        
        for css_file in css_files:
            css_path = os.path.join(source_dir, "assets", css_file)
            with open(css_path, 'r', encoding='utf-8') as f:
                css_content = f.read()
            
            # Embed in style tag
            style_tag = f'<style>\n{css_content}\n</style>'
            html_content = html_content.replace(f'assets/{css_file}', '')
            # Add style tag to head
            html_content = html_content.replace('</head>', f'{style_tag}\n</head>')
        
        # Embed images as data URLs
        for file in os.listdir(os.path.join(source_dir, "assets")):
            if file.endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg')):
                img_path = os.path.join(source_dir, "assets", file)
                with open(img_path, 'rb') as f:
                    img_data = f.read()
                
                # Convert to base64
                mime_type = self.get_mime_type(file)
                data_url = f'data:{mime_type};base64,{base64.b64encode(img_data).decode()}'
                
                # Replace in HTML
                html_content = html_content.replace(f'assets/{file}', data_url)
        
        # Save single HTML
        output_path = os.path.join(self.temp_dir, f"{self.slugify(title)}_clone.html")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return output_path
    
    async def create_multi_page_package(self, pages: List[Dict], base_url: str, options: Dict) -> Dict:
        """Create package for multiple pages"""
        package_dir = os.path.join(self.temp_dir, "multipage_website")
        os.makedirs(package_dir, exist_ok=True)
        
        # Create directory structure
        pages_dir = os.path.join(package_dir, "pages")
        assets_dir = os.path.join(package_dir, "assets")
        os.makedirs(pages_dir, exist_ok=True)
        os.makedirs(assets_dir, exist_ok=True)
        
        all_resources = {}
        downloaded_resources = set()
        
        # Process each page
        for page_idx, page in enumerate(pages):
            page_slug = self.slugify(page['title'] or f"page_{page_idx}")
            page_file = os.path.join(pages_dir, f"{page_slug}.html")
            
            # Write page HTML
            with open(page_file, 'w', encoding='utf-8') as f:
                f.write(page['content'])
            
            # Collect all resources
            for resource in page['resources']:
                all_resources[resource[1]] = resource[0]  # url -> type
        
        # Download all unique resources
        downloaded = 0
        resource_map = {}
        
        for i, (resource_url, rtype) in enumerate(all_resources.items()):
            if resource_url in downloaded_resources:
                continue
            
            try:
                content = await self.download_resource(resource_url, rtype)
                if content:
                    ext = self.get_file_extension(resource_url, rtype)
                    filename = f"resource_{i:03d}.{ext}"
                    filepath = os.path.join(assets_dir, filename)
                    
                    with open(filepath, 'wb') as f:
                        f.write(content)
                    
                    resource_map[resource_url] = f"../assets/{filename}"
                    downloaded += 1
                    downloaded_resources.add(resource_url)
            except Exception as e:
                continue
        
        # Update all HTML files with local resources
        for page_file in os.listdir(pages_dir):
            filepath = os.path.join(pages_dir, page_file)
            self.update_html_resources(filepath, resource_map)
        
        # Create main index.html with navigation
        self.create_navigation_index(package_dir, pages, base_url)
        
        # Create output
        output_path = await self.create_zip_package(package_dir, "multipage_clone")
        file_size = os.path.getsize(output_path) / (1024 * 1024) if os.path.exists(output_path) else 0
        
        return {
            'success': True,
            'title': f"Multi-page: {pages[0]['title'] if pages else 'Unknown'}",
            'output_path': output_path,
            'file_size': file_size,
            'resources_found': len(all_resources),
            'resources_downloaded': downloaded,
            'format': options.get('format', 'zip'),
            'pages': len(pages),
            'depth': options.get('max_depth', 1),
            'metadata': {
                'page_count': len(pages),
                'unique_resources': len(all_resources),
                'resource_coverage': downloaded / max(len(all_resources), 1)
            }
        }
    
    def create_navigation_index(self, base_dir: str, pages: List[Dict], base_url: str):
        """Create navigation index for multi-page sites"""
        index_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Multi-page Website Clone - EXU Cloner PRO</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .header {
            text-align: center;
            padding: 40px 20px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 20px;
            margin-bottom: 40px;
            backdrop-filter: blur(10px);
        }
        .logo {
            font-size: 48px;
            font-weight: bold;
            margin-bottom: 20px;
            background: linear-gradient(45deg, #00ff00, #00ccff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 2px 10px rgba(0, 255, 0, 0.3);
        }
        .pages-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        .page-card {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 20px;
            transition: transform 0.3s, background 0.3s;
            backdrop-filter: blur(5px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        .page-card:hover {
            transform: translateY(-5px);
            background: rgba(255, 255, 255, 0.2);
        }
        .page-card h3 {
            margin-top: 0;
            color: #00ff00;
            font-size: 18px;
        }
        .page-card a {
            display: inline-block;
            margin-top: 15px;
            padding: 10px 20px;
            background: linear-gradient(45deg, #00ff00, #00ccff);
            color: black;
            text-decoration: none;
            border-radius: 25px;
            font-weight: bold;
            transition: transform 0.2s;
        }
        .page-card a:hover {
            transform: scale(1.05);
        }
        .stats {
            background: rgba(0, 0, 0, 0.3);
            padding: 20px;
            border-radius: 15px;
            margin: 30px 0;
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
        }
        .stat-item {
            text-align: center;
            padding: 10px;
        }
        .stat-value {
            font-size: 32px;
            font-weight: bold;
            color: #00ff00;
        }
        .footer {
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid rgba(255, 255, 255, 0.2);
            color: rgba(255, 255, 255, 0.7);
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo">EXU CLONER PRO</div>
        <h1>Multi-page Website Clone</h1>
        <p>All cloned pages are listed below. Click any page to view it.</p>
    </div>
    
    <div class="stats">
        <div class="stat-item">
            <div class="stat-value">{page_count}</div>
            <div>Pages Cloned</div>
        </div>
        <div class="stat-item">
            <div class="stat-value">{resource_count}</div>
            <div>Resources</div>
        </div>
        <div class="stat-item">
            <div class="stat-value">{coverage}%</div>
            <div>Coverage</div>
        </div>
    </div>
    
    <div class="pages-grid">
        {page_cards}
    </div>
    
    <div class="footer">
        <p>Cloned with ❤️ by EXU Cloner PRO v6.0 | {timestamp}</p>
        <p>Original URL: <a href="{base_url}" style="color:#00ff00">{base_url}</a></p>
        <p>This is an offline copy of the original website.</p>
    </div>
</body>
</html>
"""
        
        # Generate page cards
        page_cards = ""
        for i, page in enumerate(pages):
            page_slug = self.slugify(page['title'] or f"page_{i}")
            page_cards += f"""
                <div class="page-card">
                    <h3>Page {i+1}: {page['title'][:50]}</h3>
                    <p>URL: {page['url'][:60]}...</p>
                    <a href="pages/{page_slug}.html">View Page →</a>
                </div>
            """
        
        # Fill template
        index_content = index_content.format(
            page_count=len(pages),
            resource_count=len(set().union(*[p['resources'] for p in pages])),
            coverage=int((len(pages) / max(len(pages), 1)) * 100),
            page_cards=page_cards,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            base_url=base_url
        )
        
        # Write index file
        index_path = os.path.join(base_dir, "index.html")
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)
    
    def update_html_resources(self, html_file: str, resource_map: Dict[str, str]):
        """Update HTML file to use local resources"""
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for old_url, new_path in resource_map.items():
            # Replace URL in various contexts
            content = content.replace(f'"{old_url}"', f'"{new_path}"')
            content = content.replace(f"'{old_url}'", f"'{new_path}'")
            content = content.replace(f'url({old_url})', f'url({new_path})')
            content = content.replace(f'={old_url}', f'={new_path}')
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def validate_url(self, url: str) -> bool:
        """Validate URL format"""
        pattern = re.compile(
            r'^(https?://)?'  # http:// or https://
            r'(([A-Z0-9][A-Z0-9-]*[A-Z0-9]\.)+[A-Z]{2,})'  # domain
            r'(:\d+)?'  # port
            r'(/.*)?$',  # path
            re.IGNORECASE
        )
        return bool(pattern.match(url))
    
    def determine_cloning_strategy(self, url: str, options: Dict) -> str:
        """Determine best cloning strategy"""
        strategy = options.get('strategy', 'auto')
        
        if strategy != 'auto':
            return strategy
        
        # Auto-detect based on URL and options
        if options.get('deep', False):
            return 'deep'
        else:
            return 'smart'
    
    async def analyze_website_type(self, url: str) -> str:
        """Analyze website to determine type"""
        try:
            headers = {'User-Agent': random.choice(Config.USER_AGENTS)}
            
            async with self.session.get(url, headers=headers, timeout=10) as response:
                content_type = response.headers.get('content-type', '')
                html_content = await response.text()
            
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Check for multiple pages
            links = soup.find_all('a', href=True)
            internal_links = [link['href'] for link in links 
                            if link['href'].startswith('/') or url in link['href']]
            
            if len(internal_links) > 5:
                return 'multi_page'
            else:
                return 'static'
                
        except:
            return 'static'
    
    def calculate_quality_score(self, result: Dict) -> int:
        """Calculate quality score for clone (0-100)"""
        if not result.get('success'):
            return 0
        
        score = 50  # Base score
        
        # Resource coverage (max 30 points)
        resources_found = result.get('resources_found', 0)
        resources_downloaded = result.get('resources_downloaded', 0)
        
        if resources_found > 0:
            coverage = resources_downloaded / resources_found
            score += int(coverage * 30)
        
        # Clone depth (max 10 points)
        pages = result.get('pages', 1)
        if pages > 1:
            score += min(pages, 10)
        
        # File size efficiency (max 10 points)
        file_size = result.get('file_size', 0)
        if file_size > 0 and file_size < 10:  # Less than 10MB
            score += 10
        elif file_size < 50:  # Less than 50MB
            score += 5
        
        # Strategy bonus (max 10 points)
        strategy = result.get('strategy', 'basic')
        if strategy in ['deep', 'smart']:
            score += 10
        
        return min(score, 100)
    
    def extract_internal_links(self, html_content: str, base_url: str) -> List[str]:
        """Extract internal links from HTML"""
        soup = BeautifulSoup(html_content, 'html.parser')
        links = soup.find_all('a', href=True)
        
        internal_links = set()
        from urllib.parse import urlparse, urljoin
        
        base_domain = urlparse(base_url).netloc
        
        for link in links:
            href = link['href']
            
            # Skip anchors, javascript, mailto, etc.
            if href.startswith(('#', 'javascript:', 'mailto:', 'tel:')):
                continue
            
            # Make absolute URL
            absolute_url = urljoin(base_url, href)
            parsed_url = urlparse(absolute_url)
            
            # Check if same domain
            if parsed_url.netloc == base_domain:
                internal_links.add(absolute_url)
        
        return list(internal_links)[:20]  # Limit to 20 links
    
    def get_file_extension(self, url: str, resource_type: str) -> str:
        """Get appropriate file extension"""
        # Try to extract from URL
        if '.' in url:
            ext = url.split('.')[-1].split('?')[0].split('#')[0]
            if len(ext) <= 5:  # Reasonable extension length
                return ext.lower()
        
        # Default extensions by type
        defaults = {
            'css': 'css',
            'js': 'js',
            'img': 'png',
            'css_img': 'png',
            'font': 'woff2'
        }
        
        return defaults.get(resource_type, 'bin')
    
    def get_mime_type(self, filename: str) -> str:
        """Get MIME type from filename"""
        extensions = {
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.gif': 'image/gif',
            '.svg': 'image/svg+xml',
            '.css': 'text/css',
            '.js': 'application/javascript',
            '.html': 'text/html',
            '.woff': 'font/woff',
            '.woff2': 'font/woff2',
            '.ttf': 'font/ttf'
        }
        
        for ext, mime in extensions.items():
            if filename.lower().endswith(ext):
                return mime
        
        return 'application/octet-stream'
    
    def slugify(self, text: str) -> str:
        """Convert text to slug"""
        text = re.sub(r'[^\w\s-]', '', text.lower())
        text = re.sub(r'[-\s]+', '-', text).strip('-')
        return text[:50]
    
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
                    print(EXUFont.log("🧹", "CLONER", f"Cleaned up: {self.temp_dir}", "INFO"))
            except Exception as e:
                print(EXUFont.log("⚠️", "CLONER", f"Cleanup error: {str(e)}", "WARNING"))
        
        asyncio.create_task(delayed_cleanup())

# ==============================================
# 𝐀𝐃𝐕𝐀𝐍𝐂𝐄𝐃 𝐁𝐎𝐓 𝐂𝐋𝐀𝐒𝐒
# ==============================================

class EXUClonerProBot:
    """Advanced EXU Cloner Bot with All Features"""
    
    def __init__(self):
        self.app = None
        self.db = AdvancedDatabase()
        self.active_clones = {}
        self.queue_processor = None
        self.start_time = datetime.now()
        
        print(EXUFont.banner())
        print(f"Builder: EXU Coder PRO | Supreme Edition")
        print(f"Start Time: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*60 + "\n")
        
        # Initialize queue processor
        self.init_queue_processor()
    
    def init_queue_processor(self):
        """Initialize batch queue processor"""
        self.queue_processor = asyncio.create_task(self.process_queue())
    
    async def process_queue(self):
        """Process batch queue"""
        while True:
            try:
                # Get pending queue items
                cursor = self.db.conn.cursor()
                cursor.execute('''
                    SELECT id, user_id, urls_json 
                    FROM queue 
                    WHERE status = 'pending' 
                    ORDER BY created_at ASC 
                    LIMIT 1
                ''')
                result = cursor.fetchone()
                
                if result:
                    queue_id, user_id, urls_json = result
                    urls = json.loads(urls_json)
                    
                    # Update status
                    cursor.execute('''
                        UPDATE queue SET status = 'processing' WHERE id = ?
                    ''', (queue_id,))
                    self.db.conn.commit()
                    
                    # Process batch
                    await self.process_batch(queue_id, user_id, urls)
                
                await asyncio.sleep(5)  # Check every 5 seconds
                
            except Exception as e:
                print(EXUFont.log("❌", "QUEUE", f"Queue processor error: {str(e)}", "ERROR"))
                await asyncio.sleep(10)
    
    async def process_batch(self, queue_id: int, user_id: int, urls: List[str]):
        """Process batch of URLs"""
        results = []
        total = len(urls)
        
        for i, url in enumerate(urls):
            try:
                # Update progress
                progress = int((i + 1) / total * 100)
                cursor = self.db.conn.cursor()
                cursor.execute('''
                    UPDATE queue SET progress = ? WHERE id = ?
                ''', (progress, queue_id))
                self.db.conn.commit()
                
                # Clone website
                result = await self.clone_website_wrapper(user_id, url, {})
                results.append(result)
                
            except Exception as e:
                results.append({
                    'url': url,
                    'success': False,
                    'error': str(e)
                })
        
        # Mark as completed
        cursor = self.db.conn.cursor()
        cursor.execute('''
            UPDATE queue SET 
                status = 'completed',
                completed_at = ?
            WHERE id = ?
        ''', (datetime.now().isoformat(), queue_id))
        self.db.conn.commit()
        
        # Send results to user
        await self.send_batch_results(user_id, queue_id, results)
    
    async def send_batch_results(self, user_id: int, queue_id: int, results: List[Dict]):
        """Send batch results to user"""
        success_count = sum(1 for r in results if r.get('success'))
        fail_count = len(results) - success_count
        
        message = f"""
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
📦 {EXUFont.bold('𝐁𝐀𝐓𝐂𝐇 𝐏𝐑𝐎𝐂𝐄𝐒𝐒𝐈𝐍𝐆 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄')}
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}

✅ {EXUFont.bold('𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥:')} {success_count}
❌ {EXUFont.bold('𝐅𝐚𝐢𝐥𝐞𝐝:')} {fail_count}
📊 {EXUFont.bold('𝐓𝐨𝐭𝐚𝐥:')} {len(results)}

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐃𝐄𝐓𝐀𝐈𝐋𝐄𝐃 𝐑𝐄𝐒𝐔𝐋𝐓𝐒:')}
"""
        
        for i, result in enumerate(results):
            status = "✅" if result.get('success') else "❌"
            message += f"\n{status} {i+1}. {result.get('url', 'Unknown')[:40]}..."
        
        message += f"\n\n{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}"
        message += f"\n📁 {EXUFont.bold('𝐐𝐮𝐞𝐮𝐞 𝐈𝐃:')} #{queue_id}"
        
        try:
            await self.app.bot.send_message(
                chat_id=user_id,
                text=message,
                parse_mode=ParseMode.MARKDOWN
            )
        except:
            pass
    
    async def clone_website_wrapper(self, user_id: int, url: str, options: Dict) -> Dict:
        """Wrapper for website cloning with user limits"""
        # Check daily limit
        if not self.db.can_clone_today(user_id):
            max_clones = self.db.get_setting('max_clones_per_day', '20')
            return {
                'success': False,
                'error': f'Daily limit reached ({max_clones}/{max_clones})'
            }
        
        # Start cloning
        cloner = None
        try:
            cloner = await AdvancedWebsiteCloner().initialize()
            
            result = await cloner.clone_website_advanced(url, options)
            
            # Record in database
            if result.get('success'):
                self.db.record_clone_advanced(user_id, {
                    **result,
                    'url': url,
                    'xp': result.get('quality_score', 10) // 10
                })
            
            return result
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
        finally:
            if cloner:
                await cloner.cleanup()
    
    # ==============================================
    # 𝐄𝐍𝐇𝐀𝐍𝐂𝐄𝐃 𝐌𝐄𝐍𝐔 𝐒𝐘𝐒𝐓𝐄𝐌
    # ==============================================
    
    def main_menu(self, user_id: int = None) -> InlineKeyboardMarkup:
        """Advanced main menu"""
        keyboard = [
            [InlineKeyboardButton("🚀 𝐂𝐥𝐨𝐧𝐞 𝐖𝐞𝐛𝐬𝐢𝐭𝐞", callback_data="clone_site")],
            [InlineKeyboardButton("📦 𝐁𝐚𝐭𝐜𝐡 𝐂𝐥𝐨𝐧𝐞", callback_data="batch_clone")],
            [
                InlineKeyboardButton("📊 𝐌𝐲 𝐏𝐫𝐨𝐟𝐢𝐥𝐞", callback_data="my_profile"),
                InlineKeyboardButton("⭐ 𝐁𝐨𝐨𝐤𝐦𝐚𝐫𝐤𝐬", callback_data="bookmarks")
            ],
            [
                InlineKeyboardButton("⚡ 𝐒𝐭𝐚𝐭𝐮𝐬", callback_data="bot_status"),
                InlineKeyboardButton("⚙️ 𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬", callback_data="user_settings")
            ],
            [InlineKeyboardButton("🆘 𝐇𝐞𝐥𝐩", callback_data="help_menu")]
        ]
        
        # Add admin button for admins
        if user_id in Config.ADMIN_IDS:
            keyboard.append([InlineKeyboardButton("👑 𝐀𝐝𝐦𝐢𝐧 𝐏𝐚𝐧𝐞𝐥", callback_data="admin_panel")])
        
        # Add verify button if not verified
        if user_id and not self.db.is_verified(user_id):
            keyboard.insert(0, [InlineKeyboardButton("🛡️ 𝐕𝐞𝐫𝐢𝐟𝐲 𝐉𝐨𝐢𝐧", callback_data="verify_join")])
        
        return InlineKeyboardMarkup(keyboard)
    
    def clone_options_menu(self) -> InlineKeyboardMarkup:
        """Clone options menu"""
        keyboard = [
            [
                InlineKeyboardButton("🔍 𝐁𝐚𝐬𝐢𝐜 𝐂𝐥𝐨𝐧𝐞", callback_data="clone_basic"),
                InlineKeyboardButton("⚡ 𝐃𝐞𝐞𝐩 𝐂𝐥𝐨𝐧𝐞", callback_data="clone_deep")
            ],
            [
                InlineKeyboardButton("🤖 𝐒𝐦𝐚𝐫𝐭 𝐂𝐥𝐨𝐧𝐞", callback_data="clone_smart"),
            ],
            [
                InlineKeyboardButton("📁 𝐅𝐨𝐫𝐦𝐚𝐭: 𝐙𝐈𝐏", callback_data="format_zip"),
                InlineKeyboardButton("📦 𝐅𝐨𝐫𝐦𝐚𝐭: 𝐓𝐀𝐑", callback_data="format_tar")
            ],
            [
                InlineKeyboardButton("🌐 𝐅𝐨𝐫𝐦𝐚𝐭: 𝐒𝐢𝐧𝐠𝐥𝐞 𝐇𝐓𝐌𝐋", callback_data="format_html"),
            ],
            [InlineKeyboardButton("◀️ 𝐁𝐚𝐜𝐤", callback_data="main_menu")]
        ]
        return InlineKeyboardMarkup(keyboard)
    
    def admin_menu(self) -> InlineKeyboardMarkup:
        """Advanced admin panel"""
        keyboard = [
            [InlineKeyboardButton("👥 𝐔𝐬𝐞𝐫 𝐌𝐚𝐧𝐚𝐠𝐞𝐦𝐞𝐧𝐭", callback_data="admin_users")],
            [InlineKeyboardButton("📊 𝐀𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐒𝐭𝐚𝐭𝐬", callback_data="admin_stats")],
            [InlineKeyboardButton("⚙️ 𝐁𝐨𝐭 𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬", callback_data="admin_settings")],
            [InlineKeyboardButton("📢 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭", callback_data="admin_broadcast")],
            [InlineKeyboardButton("🧹 𝐂𝐥𝐞𝐚𝐧𝐮𝐩", callback_data="admin_cleanup")],
            [InlineKeyboardButton("◀️ 𝐁𝐚𝐜𝐤 𝐭𝐨 𝐌𝐚𝐢𝐧", callback_data="main_menu")]
        ]
        return InlineKeyboardMarkup(keyboard)
    
    # ==============================================
    # 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 𝐇𝐀𝐍𝐃𝐋𝐄𝐑𝐒
    # ==============================================
    
    async def start_command(self, update: Update, context: CallbackContext):
        """Enhanced /start command"""
        user = update.effective_user
        
        # Add user to database with advanced features
        self.db.add_user(user.id, user.username or "", user.first_name or "")
        self.db.update_activity(user.id)
        
        # Check if banned
        if self.db.is_banned(user.id):
            await update.message.reply_text(
                f"❌ {EXUFont.bold('𝐀𝐂𝐂𝐄𝐒𝐒 𝐃𝐄𝐍𝐈𝐄𝐃')}\n\n"
                f"𝐘𝐨𝐮𝐫 𝐚𝐜𝐜𝐨𝐮𝐧𝐭 𝐡𝐚𝐬 𝐛𝐞𝐞𝐧 𝐛𝐚𝐧𝐧𝐞𝐝 𝐟𝐫𝐨𝐦 𝐭𝐡𝐢𝐬 𝐛𝐨𝐭.",
                parse_mode=ParseMode.MARKDOWN
            )
            return
        
        # Check channel verification
        force_join = self.db.get_setting('force_join', '1') == '1'
        if force_join and not self.db.is_verified(user.id):
            join_msg, keyboard = self.get_join_message()
            await update.message.reply_text(
                join_msg,
                reply_markup=keyboard,
                parse_mode=ParseMode.MARKDOWN
            )
            return
        
        # Show advanced welcome message
        welcome_msg = self.db.get_setting('welcome_msg', 
                                         '𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐄𝐗𝐔 𝐂𝐥𝐨𝐧𝐞𝐫 𝐏𝐑𝐎!')
        
        user_stats = self.db.get_user_stats_advanced(user.id)
        
        message = f"""
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐄𝐗𝐔 𝐂𝐋𝐎𝐍𝐄𝐑 𝐏𝐑𝐎')}
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}

👤 {EXUFont.bold('𝐔𝐬𝐞𝐫:')} {user.first_name}
🆔 {EXUFont.bold('𝐈𝐃:')} {user.id}
📅 {EXUFont.bold('𝐃𝐚𝐭𝐞:')} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
⭐ {EXUFont.bold('𝐋𝐞𝐯𝐞𝐥:')} {user_stats.get('level', 1)} ({user_stats.get('xp', 0)} XP)

{welcome_msg}

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐀𝐃𝐕𝐀𝐍𝐂𝐄𝐃 𝐅𝐄𝐀𝐓𝐔𝐑𝐄𝐒')}
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}

🚀 {EXUFont.bold('𝐂𝐥𝐨𝐧𝐞 𝐖𝐞𝐛𝐬𝐢𝐭𝐞')} - 𝐀𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐜𝐥𝐨𝐧𝐢𝐧𝐠 𝐰𝐢𝐭𝐡 𝐦𝐮𝐥𝐭𝐢𝐩𝐥𝐞 𝐬𝐭𝐫𝐚𝐭𝐞𝐠𝐢𝐞𝐬
📦 {EXUFont.bold('𝐁𝐚𝐭𝐜𝐡 𝐂𝐥𝐨𝐧𝐞')} - 𝐂𝐥𝐨𝐧𝐞 𝐦𝐮𝐥𝐭𝐢𝐩𝐥𝐞 𝐰𝐞𝐛𝐬𝐢𝐭𝐞𝐬 𝐚𝐭 𝐨𝐧𝐜𝐞
📊 {EXUFont.bold('𝐌𝐲 𝐏𝐫𝐨𝐟𝐢𝐥𝐞')} - 𝐃𝐞𝐭𝐚𝐢𝐥𝐞𝐝 𝐬𝐭𝐚𝐭𝐬 𝐚𝐧𝐝 𝐚𝐜𝐡𝐢𝐞𝐯𝐞𝐦𝐞𝐧𝐭𝐬
⭐ {EXUFont.bold('𝐁𝐨𝐨𝐤𝐦𝐚𝐫𝐤𝐬')} - 𝐒𝐚𝐯𝐞 𝐟𝐚𝐯𝐨𝐫𝐢𝐭𝐞 𝐰𝐞𝐛𝐬𝐢𝐭𝐞𝐬
⚡ {EXUFont.bold('𝐒𝐭𝐚𝐭𝐮𝐬')} - 𝐑𝐞𝐚𝐥-𝐭𝐢𝐦𝐞 𝐛𝐨𝐭 𝐬𝐭𝐚𝐭𝐮𝐬 𝐚𝐧𝐝 𝐚𝐧𝐚𝐥𝐲𝐭𝐢𝐜𝐬
⚙️ {EXUFont.bold('𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬')} - 𝐂𝐮𝐬𝐭𝐨𝐦𝐢𝐳𝐞 𝐲𝐨𝐮𝐫 𝐞𝐱𝐩𝐞𝐫𝐢𝐞𝐧𝐜𝐞

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('📊 𝐘𝐎𝐔𝐑 𝐒𝐓𝐀𝐓𝐒:')}
• 𝐓𝐨𝐭𝐚𝐥 𝐂𝐥𝐨𝐧𝐞𝐬: {user_stats.get('total_clones', 0)}
• 𝐂𝐥𝐨𝐧𝐞𝐬 𝐓𝐨𝐝𝐚𝐲: {user_stats.get('clones_today', 0)}/{self.db.get_setting('max_clones_per_day', '20')}
• 𝐒𝐮𝐜𝐜𝐞𝐬𝐬 𝐑𝐚𝐭𝐞: {user_stats.get('success_rate', 0):.1f}%
• 𝐒𝐭𝐨𝐫𝐚𝐠𝐞 𝐔𝐬𝐞𝐝: {user_stats.get('total_storage', 0):.1f} MB

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐁𝐮𝐢𝐥𝐝𝐞𝐫: 𝐄𝐗𝐔 𝐂𝐨𝐝𝐞𝐫 𝐏𝐑𝐎')}
"""
        
        await update.message.reply_text(
            message,
            reply_markup=self.main_menu(user.id),
            parse_mode=ParseMode.MARKDOWN
        )
    
    def get_join_message(self) -> tuple:
        """Get enhanced channel join message"""
        message = f"""
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐕𝐄𝐑𝐈𝐅𝐈𝐂𝐀𝐓𝐈𝐎𝐍 𝐑𝐄𝐐𝐔𝐈𝐑𝐄𝐃')}
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}

📢 {EXUFont.bold('𝐉𝐨𝐢𝐧 𝐨𝐮𝐫 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐭𝐨 𝐮𝐬𝐞 𝐭𝐡𝐢𝐬 𝐛𝐨𝐭:')}
{Config.CHANNEL_USERNAME}

💬 {EXUFont.bold('𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩:')}
{Config.SUPPORT_GROUP}

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐈𝐧𝐬𝐭𝐫𝐮𝐜𝐭𝐢𝐨𝐧𝐬:')}
1. 𝐂𝐥𝐢𝐜𝐤 "📢 𝐉𝐨𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥" 𝐛𝐮𝐭𝐭𝐨𝐧
2. 𝐉𝐨𝐢𝐧 𝐭𝐡𝐞 𝐜𝐡𝐚𝐧𝐧𝐞𝐥
3. 𝐂𝐥𝐢𝐜𝐤 "✅ 𝐈'𝐯𝐞 𝐉𝐨𝐢𝐧𝐞𝐝"
4. 𝐁𝐨𝐭 𝐰𝐢𝐥𝐥 𝐯𝐞𝐫𝐢𝐟𝐲 𝐲𝐨𝐮𝐫 𝐦𝐞𝐦𝐛𝐞𝐫𝐬𝐡𝐢𝐩
5. 𝐆𝐞𝐭 𝐚𝐜𝐜𝐞𝐬𝐬 𝐭𝐨 𝐚𝐥𝐥 𝐟𝐞𝐚𝐭𝐮𝐫𝐞𝐬!

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
✨ {EXUFont.bold('𝐁𝐞𝐧𝐞𝐟𝐢𝐭𝐬:')}
• 𝐀𝐜𝐜𝐞𝐬𝐬 𝐭𝐨 𝐄𝐗𝐔 𝐂𝐥𝐨𝐧𝐞𝐫 𝐏𝐑𝐎
• 𝐄𝐱𝐜𝐥𝐮𝐬𝐢𝐯𝐞 𝐮𝐩𝐝𝐚𝐭𝐞𝐬 𝐚𝐧𝐝 𝐟𝐞𝐚𝐭𝐮𝐫𝐞𝐬
• 𝐏𝐫𝐢𝐨𝐫𝐢𝐭𝐲 𝐬𝐮𝐩𝐩𝐨𝐫𝐭
• 𝐃𝐚𝐢𝐥𝐲 𝐭𝐢𝐩𝐬 𝐚𝐧𝐝 𝐭𝐮𝐭𝐨𝐫𝐢𝐚𝐥𝐬
"""
        
        keyboard = [
            [InlineKeyboardButton("📢 𝐉𝐨𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", 
                                 url=f"https://t.me/{Config.CHANNEL_USERNAME.lstrip('@')}")],
            [InlineKeyboardButton("💬 𝐉𝐨𝐢𝐧 𝐒𝐮𝐩𝐩𝐨𝐫𝐭", 
                                 url=f"https://t.me/{Config.SUPPORT_GROUP.lstrip('@')}")],
            [InlineKeyboardButton("✅ 𝐈'𝐯𝐞 𝐉𝐨𝐢𝐧𝐞𝐝", callback_data="verify_join")]
        ]
        
        return message, InlineKeyboardMarkup(keyboard)
    
    async def callback_handler(self, update: Update, context: CallbackContext):
        """Enhanced callback handler"""
        query = update.callback_query
        await query.answer()
        
        user_id = query.from_user.id
        data = query.data
        
        print(EXUFont.log("📱", "BUTTON", f"User {user_id} pressed: {data}", "INFO"))
        
        # Update activity
        self.db.update_activity(user_id)
        
        # Handle callbacks
        handlers = {
            "main_menu": self.show_main_menu,
            "verify_join": self.verify_user,
            "clone_site": self.start_cloning,
            "batch_clone": self.start_batch_cloning,
            "my_profile": self.show_profile,
            "bookmarks": self.show_bookmarks,
            "bot_status": self.show_bot_status,
            "user_settings": self.show_user_settings,
            "help_menu": self.show_help,
            "admin_panel": self.show_admin_panel,
            "clone_basic": lambda q: self.set_clone_strategy(q, "basic"),
            "clone_deep": lambda q: self.set_clone_strategy(q, "deep"),
            "clone_smart": lambda q: self.set_clone_strategy(q, "smart"),
            "format_zip": lambda q: self.set_output_format(q, "zip"),
            "format_tar": lambda q: self.set_output_format(q, "tar.gz"),
            "format_html": lambda q: self.set_output_format(q, "single_html"),
        }
        
        if data in handlers:
            await handlers[data](query)
        elif data.startswith("admin_"):
            await self.handle_admin_callback(query, context, data, user_id)
        elif data.startswith("bookmark_"):
            await self.handle_bookmark_callback(query, data, user_id)
        else:
            await query.answer("⚡ 𝐅𝐞𝐚𝐭𝐮𝐫𝐞 𝐜𝐨𝐦𝐢𝐧𝐠 𝐬𝐨𝐨𝐧!", show_alert=True)
    
    async def set_clone_strategy(self, query, strategy: str):
        """Set cloning strategy"""
        user_id = query.from_user.id
        
        if user_id not in self.active_clones:
            self.active_clones[user_id] = {}
        
        self.active_clones[user_id]['strategy'] = strategy
        
        strategies = {
            'basic': '🔍 𝐁𝐚𝐬𝐢𝐜 𝐂𝐥𝐨𝐧𝐞',
            'deep': '⚡ 𝐃𝐞𝐞𝐩 𝐂𝐥𝐨𝐧𝐞',
            'smart': '🤖 𝐒𝐦𝐚𝐫𝐭 𝐂𝐥𝐨𝐧𝐞'
        }
        
        await query.answer(f"✅ 𝐒𝐭𝐫𝐚𝐭𝐞𝐠𝐲 𝐬𝐞𝐭: {strategies[strategy]}", show_alert=True)
    
    async def set_output_format(self, query, format: str):
        """Set output format"""
        user_id = query.from_user.id
        
        if user_id not in self.active_clones:
            self.active_clones[user_id] = {}
        
        self.active_clones[user_id]['format'] = format
        
        formats = {
            'zip': '📁 𝐙𝐈𝐏',
            'tar.gz': '📦 𝐓𝐀𝐑.𝐆𝐙',
            'single_html': '🌐 𝐒𝐢𝐧𝐠𝐥𝐞 𝐇𝐓𝐌𝐋'
        }
        
        await query.answer(f"✅ 𝐅𝐨𝐫𝐦𝐚𝐭 𝐬𝐞𝐭: {formats[format]}", show_alert=True)
    
    async def start_cloning(self, query):
        """Start advanced cloning process"""
        user_id = query.from_user.id
        
        # Check verification
        force_join = self.db.get_setting('force_join', '1') == '1'
        if force_join and not self.db.is_verified(user_id):
            join_msg, keyboard = self.get_join_message()
            await query.edit_message_text(
                join_msg,
                reply_markup=keyboard,
                parse_mode=ParseMode.MARKDOWN
            )
            return
        
        # Check daily limit
        if not self.db.can_clone_today(user_id):
            max_clones = self.db.get_setting('max_clones_per_day', '20')
            await query.answer(
                f"❌ 𝐃𝐚𝐢𝐥𝐲 𝐥𝐢𝐦𝐢𝐭 𝐫𝐞𝐚𝐜𝐡𝐞𝐝! ({max_clones}/{max_clones})",
                show_alert=True
            )
            return
        
        user_stats = self.db.get_user_stats_advanced(user_id)
        
        await query.edit_message_text(
            f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
            f"🚀 {EXUFont.bold('𝐀𝐃𝐕𝐀𝐍𝐂𝐄𝐃 𝐂𝐋𝐎𝐍𝐈𝐍𝐆')}\n"
            f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n\n"
            f"📝 {EXUFont.bold('𝐏𝐥𝐞𝐚𝐬𝐞 𝐬𝐞𝐧𝐝 𝐭𝐡𝐞 𝐔𝐑𝐋 𝐲𝐨𝐮 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐜𝐥𝐨𝐧𝐞:')}\n\n"
            f"{EXUFont.bold('𝐄𝐱𝐚𝐦𝐩𝐥𝐞𝐬:')}\n"
            f"• https://example.com\n"
            f"• https://github.com\n"
            f"• https://wikipedia.org\n\n"
            f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
            f"⚡ {EXUFont.bold('𝐂𝐥𝐨𝐧𝐢𝐧𝐠 𝐎𝐩𝐭𝐢𝐨𝐧𝐬:')}\n"
            f"• 𝐁𝐚𝐬𝐢𝐜 - 𝐒𝐢𝐦𝐩𝐥𝐞 𝐇𝐓𝐌𝐋/𝐂𝐒𝐒/𝐉𝐒\n"
            f"• 𝐃𝐞𝐞𝐩 - 𝐌𝐮𝐥𝐭𝐢-𝐩𝐚𝐠𝐞 𝐜𝐥𝐨𝐧𝐢𝐧𝐠\n"
            f"• 𝐒𝐦𝐚𝐫𝐭 - 𝐀𝐮𝐭𝐨-𝐝𝐞𝐭𝐞𝐜𝐭 𝐛𝐞𝐬𝐭 𝐬𝐭𝐫𝐚𝐭𝐞𝐠𝐲\n\n"
            f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
            f"⚠️ {EXUFont.bold('𝐋𝐢𝐦𝐢𝐭𝐬:')}\n"
            f"• 𝐌𝐚𝐱 𝐟𝐢𝐥𝐞 𝐬𝐢𝐳𝐞: {Config.MAX_CLONE_SIZE_MB} MB\n"
            f"• 𝐂𝐥𝐨𝐧𝐞𝐬 𝐭𝐨𝐝𝐚𝐲: {user_stats.get('clones_today', 0)}/{self.db.get_setting('max_clones_per_day', '20')}\n"
            f"• 𝐌𝐚𝐱 𝐩𝐚𝐠𝐞𝐬 (𝐝𝐞𝐞𝐩): {Config.MAX_PAGES_PER_CLONE}\n"
            f"• 𝐌𝐚𝐱 𝐝𝐞𝐩𝐭𝐡: {Config.MAX_DEPTH}",
            reply_markup=self.clone_options_menu(),
            parse_mode=ParseMode.MARKDOWN
        )
        
        # Store that we're waiting for URL
        self.active_clones[user_id] = {
            "state": "waiting_url",
            "strategy": "smart",
            "format": self.db.get_setting('default_format', 'zip')
        }
    
    async def start_batch_cloning(self, query):
        """Start batch cloning"""
        user_id = query.from_user.id
        
        # Check verification
        force_join = self.db.get_setting('force_join', '1') == '1'
        if force_join and not self.db.is_verified(user_id):
            join_msg, keyboard = self.get_join_message()
            await query.edit_message_text(
                join_msg,
                reply_markup=keyboard,
                parse_mode=ParseMode.MARKDOWN
            )
            return
        
        await query.edit_message_text(
            f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
            f"📦 {EXUFont.bold('𝐁𝐀𝐓𝐂𝐇 𝐂𝐋𝐎𝐍𝐈𝐍𝐆')}\n"
            f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n\n"
            f"📝 {EXUFont.bold('𝐒𝐞𝐧𝐝 𝐦𝐮𝐥𝐭𝐢𝐩𝐥𝐞 𝐔𝐑𝐋𝐬 𝐭𝐨 𝐜𝐥𝐨𝐧𝐞:')}\n\n"
            f"{EXUFont.bold('𝐅𝐨𝐫𝐦𝐚𝐭:')}\n"
            f"• 𝐎𝐧𝐞 𝐔𝐑𝐋 𝐩𝐞𝐫 𝐥𝐢𝐧𝐞\n"
            f"• 𝐌𝐚𝐱 𝟏𝟎 𝐔𝐑𝐋𝐬 𝐩𝐞𝐫 𝐛𝐚𝐭𝐜𝐡\n"
            f"• 𝐄𝐚𝐜𝐡 𝐔𝐑𝐋 𝐨𝐧 𝐚 𝐬𝐞𝐩𝐚𝐫𝐚𝐭𝐞 𝐥𝐢𝐧𝐞\n\n"
            f"{EXUFont.bold('𝐄𝐱𝐚𝐦𝐩𝐥𝐞:')}\n"
            f"https://example.com\n"
            f"https://github.com\n"
            f"https://wikipedia.org\n\n"
            f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
            f"⚡ {EXUFont.bold('𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬:')}\n"
            f"• 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐢𝐧 𝐭𝐡𝐞 𝐛𝐚𝐜𝐤𝐠𝐫𝐨𝐮𝐧𝐝\n"
            f"• 𝐆𝐞𝐭 𝐧𝐨𝐭𝐢𝐟𝐢𝐞𝐝 𝐰𝐡𝐞𝐧 𝐜𝐨𝐦𝐩𝐥𝐞𝐭𝐞\n"
            f"• 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐞𝐚𝐜𝐡 𝐜𝐥𝐨𝐧𝐞 𝐬𝐞𝐩𝐚𝐫𝐚𝐭𝐞𝐥𝐲\n"
            f"• 𝐕𝐢𝐞𝐰 𝐩𝐫𝐨𝐠𝐫𝐞𝐬𝐬 𝐢𝐧 𝐫𝐞𝐚𝐥-𝐭𝐢𝐦𝐞",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("◀️ 𝐂𝐚𝐧𝐜𝐞𝐥", callback_data="main_menu")]
            ]),
            parse_mode=ParseMode.MARKDOWN
        )
        
        # Store that we're waiting for batch URLs
        self.active_clones[user_id] = {"state": "waiting_batch"}
    
    async def handle_url_message(self, update: Update, context: CallbackContext):
        """Handle URL messages for cloning"""
        user_id = update.effective_user.id
        
        if user_id in self.active_clones:
            state = self.active_clones[user_id].get("state")
            
            if state == "waiting_url":
                url = update.message.text.strip()
                
                # Validate URL
                if not url.startswith(('http://', 'https://')):
                    url = 'https://' + url
                
                # Get cloning options
                options = {
                    'strategy': self.active_clones[user_id].get('strategy', 'smart'),
                    'format': self.active_clones[user_id].get('format', 'zip'),
                    'max_pages': Config.MAX_PAGES_PER_CLONE,
                    'max_depth': Config.MAX_DEPTH
                }
                
                # Start cloning
                await self.process_advanced_clone(update, url, user_id, options)
                
            elif state == "waiting_batch":
                urls = update.message.text.strip().split('\n')
                urls = [url.strip() for url in urls if url.strip()]
                
                # Limit to 10 URLs
                urls = urls[:10]
                
                # Validate URLs
                valid_urls = []
                for url in urls:
                    if not url.startswith(('http://', 'https://')):
                        url = 'https://' + url
                    valid_urls.append(url)
                
                # Add to queue
                queue_id = self.db.add_to_queue(user_id, valid_urls)
                
                await update.message.reply_text(
                    f"📦 {EXUFont.bold('𝐁𝐀𝐓𝐂𝐇 𝐐𝐔𝐄𝐔𝐄𝐃')}\n\n"
                    f"✅ {EXUFont.bold('𝐁𝐚𝐭𝐜𝐡 𝐚𝐝𝐝𝐞𝐝 𝐭𝐨 𝐪𝐮𝐞𝐮𝐞!')}\n\n"
                    f"📊 {EXUFont.bold('𝐃𝐞𝐭𝐚𝐢𝐥𝐬:')}\n"
                    f"• 𝐐𝐮𝐞𝐮𝐞 𝐈𝐃: #{queue_id}\n"
                    f"• 𝐔𝐑𝐋𝐬: {len(valid_urls)}\n"
                    f"• 𝐒𝐭𝐚𝐭𝐮𝐬: ⏳ 𝐏𝐞𝐧𝐝𝐢𝐧𝐠\n\n"
                    f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
                    f"⚡ {EXUFont.bold('𝐍𝐨𝐭𝐞:')}\n"
                    f"𝐘𝐨𝐮 𝐰𝐢𝐥𝐥 𝐫𝐞𝐜𝐞𝐢𝐯𝐞 𝐚 𝐧𝐨𝐭𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧 𝐰𝐡𝐞𝐧 𝐚𝐥𝐥 𝐜𝐥𝐨𝐧𝐞𝐬 𝐚𝐫𝐞 𝐜𝐨𝐦𝐩𝐥𝐞𝐭𝐞.",
                    reply_markup=self.main_menu(user_id),
                    parse_mode=ParseMode.MARKDOWN
                )
                
                # Clear state
                if user_id in self.active_clones:
                    del self.active_clones[user_id]
        else:
            # Send to main menu
            await self.start_command(update, context)
    
    async def process_advanced_clone(self, update: Update, url: str, user_id: int, options: Dict):
        """Process advanced website cloning"""
        # Create status message with animation
        status_msg = await update.message.reply_text(
            f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
            f"⚡ {EXUFont.bold('𝐂𝐘𝐁𝐄𝐑 𝐂𝐋𝐎𝐍𝐈𝐍𝐆 𝐒𝐓𝐀𝐑𝐓𝐄𝐃')}\n"
            f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n\n"
            f"🔗 {EXUFont.bold('𝐔𝐑𝐋:')} {url[:50]}...\n"
            f"👤 {EXUFont.bold('𝐔𝐬𝐞𝐫:')} {update.effective_user.first_name}\n"
            f"🎯 {EXUFont.bold('𝐒𝐭𝐫𝐚𝐭𝐞𝐠𝐲:')} {options.get('strategy', 'smart').upper()}\n"
            f"📁 {EXUFont.bold('𝐅𝐨𝐫𝐦𝐚𝐭:')} {options.get('format', 'zip').upper()}\n\n"
            f"⚡ {EXUFont.bold('𝐄𝐱𝐞𝐜𝐮𝐭𝐢𝐧𝐠:')} [▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱] 0%\n\n"
            f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
            f"⏳ {EXUFont.bold('𝐏𝐥𝐞𝐚𝐬𝐞 𝐰𝐚𝐢𝐭, 𝐭𝐡𝐢𝐬 𝐦𝐚𝐲 𝐭𝐚𝐤𝐞 𝐚 𝐟𝐞𝐰 𝐦𝐢𝐧𝐮𝐭𝐞𝐬...')}",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("❌ 𝐂𝐚𝐧𝐜𝐞𝐥", callback_data=f"cancel_{user_id}")]
            ]),
            parse_mode=ParseMode.MARKDOWN
        )
        
        # Start clone task
        task = asyncio.create_task(
            self.execute_advanced_clone(update, url, status_msg, user_id, options)
        )
        self.active_clones[user_id] = {
            "task": task,
            "url": url,
            "start_time": datetime.now(),
            "status_msg": status_msg,
            "options": options
        }
    
    async def execute_advanced_clone(self, update: Update, url: str, status_msg, 
                                   user_id: int, options: Dict):
        """Execute the advanced cloning process"""
        cloner = None
        
        try:
            # Show progress animation
            await AdvancedAnimationEngine.progress_animation(
                status_msg,
                f"𝐂𝐥𝐨𝐧𝐢𝐧𝐠: {url[:40]}...",
                duration=2.0,
                style="cyber"
            )
            
            # Initialize advanced cloner
            cloner = await AdvancedWebsiteCloner().initialize()
            
            # Clone website
            result = await cloner.clone_website_advanced(url, options)
            
            if not result['success']:
                await self.update_clone_status(
                    status_msg, 
                    f"❌ {EXUFont.bold('𝐂𝐋𝐎𝐍𝐈𝐍𝐆 𝐅𝐀𝐈𝐋𝐄𝐃')}\n\n"
                    f"𝐄𝐫𝐫𝐨𝐫: {result['error'][:100]}...",
                    progress=0,
                    error=True
                )
                return
            
            # Show success animation
            await AdvancedAnimationEngine.progress_animation(
                status_msg,
                f"✅ 𝐂𝐥𝐨𝐧𝐞 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥: {result['title'][:30]}...",
                duration=1.0,
                style="blocks"
            )
            
            # Calculate stats
            time_taken = (datetime.now() - self.active_clones[user_id]['start_time']).total_seconds()
            
            # Generate preview image
            preview_image = None
            if self.db.get_setting('enable_preview', '1') == '1':
                try:
                    preview_image = AdvancedAnimationEngine.create_preview_image(
                        url, 
                        result['title']
                    )
                except:
                    pass
            
            # Send success message
            success_text = f"""
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
✅ {EXUFont.bold('𝐂𝐋𝐎𝐍𝐈𝐍𝐆 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄!')}
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}

📄 {EXUFont.bold('𝐓𝐢𝐭𝐥𝐞:')} {result['title'][:50]}
🔗 {EXUFont.bold('𝐔𝐑𝐋:')} {url[:50]}...
📊 {EXUFont.bold('𝐒𝐭𝐫𝐚𝐭𝐞𝐠𝐲:')} {result.get('strategy', 'basic').upper()}
📁 {EXUFont.bold('𝐅𝐨𝐫𝐦𝐚𝐭:')} {result.get('format', 'zip').upper()}

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
📈 {EXUFont.bold('𝐒𝐓𝐀𝐓𝐒:')}

📦 𝐅𝐢𝐥𝐞 𝐒𝐢𝐳𝐞: {result['file_size']:.2f} MB
📊 𝐑𝐞𝐬𝐨𝐮𝐫𝐜𝐞𝐬: {result['resources_downloaded']}/{result['resources_found']}
⭐ 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐒𝐜𝐨𝐫𝐞: {result.get('quality_score', 0)}/100
⏱️ 𝐓𝐢𝐦𝐞: {time_taken:.1f}𝐬

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
🎯 {EXUFont.bold('𝐀𝐂𝐓𝐈𝐎𝐍𝐒:')}
"""
            
            keyboard = [
                [
                    InlineKeyboardButton("💾 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝", callback_data=f"download_{user_id}"),
                    InlineKeyboardButton("⭐ 𝐁𝐨𝐨𝐤𝐦𝐚𝐫𝐤", callback_data=f"bookmark_{url}")
                ],
                [
                    InlineKeyboardButton("🔄 𝐍𝐞𝐰 𝐂𝐥𝐨𝐧𝐞", callback_data="clone_site"),
                    InlineKeyboardButton("🏠 𝐌𝐚𝐢𝐧 𝐌𝐞𝐧𝐮", callback_data="main_menu")
                ]
            ]
            
            await status_msg.edit_text(
                success_text,
                reply_markup=InlineKeyboardMarkup(keyboard),
                parse_mode=ParseMode.MARKDOWN
            )
            
            # Send preview image if available
            if preview_image:
                try:
                    await update.message.reply_photo(
                        photo=preview_image,
                        caption=f"📸 {EXUFont.bold('𝐏𝐑𝐄𝐕𝐈𝐄𝐖:')} {result['title'][:50]}",
                        reply_markup=self.main_menu(user_id)
                    )
                except:
                    pass
            
            # Store result for download
            self.active_clones[user_id]['result'] = result
            
        except Exception as e:
            # Record failure
            print(EXUFont.log("❌", "CLONER", f"Advanced clone failed: {str(e)}", "ERROR"))
            
            await self.update_clone_status(
                status_msg,
                f"❌ {EXUFont.bold('𝐂𝐋𝐎𝐍𝐈𝐍𝐆 𝐅𝐀𝐈𝐋𝐄𝐃')}\n\n"
                f"💥 {EXUFont.bold('𝐄𝐫𝐫𝐨𝐫:')} {str(e)[:100]}...\n\n"
                f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
                f"⚠️ {EXUFont.bold('𝐓𝐫𝐨𝐮𝐛𝐥𝐞𝐬𝐡𝐨𝐨𝐭𝐢𝐧𝐠:')}\n"
                f"• 𝐔𝐬𝐞 𝐚 𝐬𝐢𝐦𝐩𝐥𝐞𝐫 𝐰𝐞𝐛𝐬𝐢𝐭𝐞\n"
                f"• 𝐓𝐫𝐲 𝐛𝐚𝐬𝐢𝐜 𝐜𝐥𝐨𝐧𝐢𝐧𝐠 𝐬𝐭𝐫𝐚𝐭𝐞𝐠𝐲\n"
                f"• 𝐂𝐡𝐞𝐜𝐤 𝐭𝐡𝐞 𝐔𝐑𝐋 𝐢𝐬 𝐜𝐨𝐫𝐫𝐞𝐜𝐭\n"
                f"• 𝐓𝐫𝐲 𝐚𝐠𝐚𝐢𝐧 𝐥𝐚𝐭𝐞𝐫",
                progress=0,
                error=True
            )
            
        finally:
            if cloner:
                await cloner.cleanup()
    
    async def update_clone_status(self, message, text: str, progress: float, error: bool = False):
        """Update clone status with EXU style"""
        bar = EXUFont.create_progress(progress, style="cyber")
        
        try:
            if not error:
                await message.edit_text(
                    f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
                    f"⚡ {EXUFont.bold('𝐂𝐘𝐁𝐄𝐑 𝐂𝐋𝐎𝐍𝐈𝐍𝐆')}\n"
                    f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n\n"
                    f"{bar}\n\n"
                    f"{text}\n\n"
                    f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
                    f"⏳ {EXUFont.bold('𝐏𝐥𝐞𝐚𝐬𝐞 𝐰𝐚𝐢𝐭...')}",
                    parse_mode=ParseMode.MARKDOWN
                )
            else:
                await message.edit_text(
                    f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
                    f"❌ {EXUFont.bold('𝐂𝐋𝐎𝐍𝐈𝐍𝐆 𝐅𝐀𝐈𝐋𝐄𝐃')}\n"
                    f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n\n"
                    f"{text}",
                    parse_mode=ParseMode.MARKDOWN
                )
        except:
            pass
        
        await asyncio.sleep(0.5)
    
    async def show_profile(self, query):
        """Show advanced user profile"""
        user_id = query.from_user.id
        user_stats = self.db.get_user_stats_advanced(user_id)
        verified = self.db.is_verified(user_id)
        
        # Calculate level progress
        xp_needed = user_stats.get('level', 1) * 100
        xp_current = user_stats.get('xp', 0) % 100
        level_progress = xp_current / xp_needed * 100 if xp_needed > 0 else 0
        
        profile_text = f"""
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
📊 {EXUFont.bold('𝐌𝐘 𝐀𝐃𝐕𝐀𝐍𝐂𝐄𝐃 𝐏𝐑𝐎𝐅𝐈𝐋𝐄')}
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}

👤 {EXUFont.bold('𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞:')} @{user_stats.get('username', 'N/A')}
📛 {EXUFont.bold('𝐍𝐚𝐦𝐞:')} {user_stats.get('name', 'User')}
🆔 {EXUFont.bold('𝐈𝐃:')} {user_id}
📅 {EXUFont.bold('𝐉𝐨𝐢𝐧𝐞𝐝:')} {user_stats.get('join_date', 'N/A')}
🛡️ {EXUFont.bold('𝐒𝐭𝐚𝐭𝐮𝐬:')} {'✅ 𝐕𝐞𝐫𝐢𝐟𝐢𝐞𝐝' if verified else '⭕ 𝐏𝐞𝐧𝐝𝐢𝐧𝐠'}

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
⭐ {EXUFont.bold('𝐋𝐄𝐕𝐄𝐋 & 𝐏𝐑𝐎𝐆𝐑𝐄𝐒𝐒:')}

🏆 𝐋𝐞𝐯𝐞𝐥: {user_stats.get('level', 1)}
⚡ 𝐗𝐏: {user_stats.get('xp', 0)} / {user_stats.get('level', 1) * 100}
📊 𝐏𝐫𝐨𝐠𝐫𝐞𝐬𝐬: {EXUFont.create_progress(level_progress/100, 10)}

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
🚀 {EXUFont.bold('𝐂𝐋𝐎𝐍𝐈𝐍𝐆 𝐒𝐓𝐀𝐓𝐒:')}

📈 𝐓𝐨𝐭𝐚𝐥 𝐂𝐥𝐨𝐧𝐞𝐬: {user_stats.get('total_clones', 0)}
📊 𝐂𝐥𝐨𝐧𝐞𝐬 𝐓𝐨𝐝𝐚𝐲: {user_stats.get('clones_today', 0)}/{self.db.get_setting('max_clones_per_day', '20')}
✅ 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥: {user_stats.get('success_count', 0)}
🎯 𝐒𝐮𝐜𝐜𝐞𝐬𝐬 𝐑𝐚𝐭𝐞: {user_stats.get('success_rate', 0):.1f}%
💾 𝐒𝐭𝐨𝐫𝐚𝐠𝐞 𝐔𝐬𝐞𝐝: {user_stats.get('total_storage', 0):.1f} MB
⭐ 𝐀𝐯𝐠 𝐐𝐮𝐚𝐥𝐢𝐭𝐲: {user_stats.get('avg_quality', 0):.1f}/100

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
🎮 {EXUFont.bold('𝐀𝐂𝐇𝐈𝐄𝐕𝐄𝐌𝐄𝐍𝐓𝐒:')}
"""
        
        # Add achievements based on stats
        achievements = []
        
        if user_stats.get('total_clones', 0) >= 10:
            achievements.append("🏆 𝐂𝐥𝐨𝐧𝐞𝐫 𝐍𝐨𝐯𝐢𝐜𝐞 (10+ clones)")
        if user_stats.get('total_clones', 0) >= 50:
            achievements.append("🏆 𝐂𝐥𝐨𝐧𝐢𝐧𝐠 𝐌𝐚𝐬𝐭𝐞𝐫 (50+ clones)")
        if user_stats.get('success_rate', 0) >= 90:
            achievements.append("🎯 𝐏𝐞𝐫𝐟𝐞𝐜𝐭 𝐂𝐥𝐨𝐧𝐞𝐫 (90%+ success rate)")
        if user_stats.get('avg_quality', 0) >= 80:
            achievements.append("⭐ 𝐇𝐢𝐠𝐡-𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐂𝐥𝐨𝐧𝐞𝐫 (80+ avg quality)")
        
        for achievement in achievements:
            profile_text += f"• {achievement}\n"
        
        if not achievements:
            profile_text += "• 𝐍𝐨 𝐚𝐜𝐡𝐢𝐞𝐯𝐞𝐦𝐞𝐧𝐭𝐬 𝐲𝐞𝐭. 𝐊𝐞𝐞𝐩 𝐜𝐥𝐨𝐧𝐢𝐧𝐠!\n"
        
        profile_text += f"\n{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}"
        
        keyboard = [[InlineKeyboardButton("🔄 𝐑𝐞𝐟𝐫𝐞𝐬𝐡", callback_data="my_profile")]]
        if not verified:
            keyboard.append([InlineKeyboardButton("🛡️ 𝐕𝐞𝐫𝐢𝐟𝐲 𝐉𝐨𝐢𝐧", callback_data="verify_join")])
        keyboard.append([InlineKeyboardButton("◀️ 𝐁𝐚𝐜𝐤", callback_data="main_menu")])
        
        await query.edit_message_text(
            profile_text,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode=ParseMode.MARKDOWN
        )
    
    async def show_bookmarks(self, query):
        """Show user bookmarks"""
        user_id = query.from_user.id
        bookmarks = self.db.get_bookmarks(user_id)
        
        if not bookmarks:
            await query.edit_message_text(
                f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
                f"⭐ {EXUFont.bold('𝐘𝐎𝐔𝐑 𝐁𝐎𝐎𝐊𝐌𝐀𝐑𝐊𝐒')}\n"
                f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n\n"
                f"📭 {EXUFont.bold('𝐍𝐨 𝐛𝐨𝐨𝐤𝐦𝐚𝐫𝐤𝐬 𝐲𝐞𝐭!')}\n\n"
                f"𝐓𝐨 𝐚𝐝𝐝 𝐚 𝐛𝐨𝐨𝐤𝐦𝐚𝐫𝐤:\n"
                f"1. 𝐂𝐥𝐨𝐧𝐞 𝐚 𝐰𝐞𝐛𝐬𝐢𝐭𝐞\n"
                f"2. 𝐂𝐥𝐢𝐜𝐤 '⭐ 𝐁𝐨𝐨𝐤𝐦𝐚𝐫𝐤' 𝐛𝐮𝐭𝐭𝐨𝐧\n"
                f"3. 𝐈𝐭 𝐰𝐢𝐥𝐥 𝐚𝐩𝐩𝐞𝐚𝐫 𝐡𝐞𝐫𝐞",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("🚀 𝐂𝐥𝐨𝐧𝐞 𝐖𝐞𝐛𝐬𝐢𝐭𝐞", callback_data="clone_site")],
                    [InlineKeyboardButton("◀️ 𝐁𝐚𝐜𝐤", callback_data="main_menu")]
                ]),
                parse_mode=ParseMode.MARKDOWN
            )
            return
        
        # Create bookmark list
        bookmark_text = f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
        bookmark_text += f"⭐ {EXUFont.bold('𝐘𝐎𝐔𝐑 𝐁𝐎𝐎𝐊𝐌𝐀𝐑𝐊𝐒')} ({len(bookmarks)})\n"
        bookmark_text += f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n\n"
        
        keyboard = []
        
        for i, bookmark in enumerate(bookmarks[:10]):  # Show first 10
            url = bookmark.get('url', '')
            title = bookmark.get('title', 'Untitled')
            added = bookmark.get('added', '')
            
            # Shorten URL for display
            display_url = url[:40] + "..." if len(url) > 40 else url
            
            bookmark_text += f"🔖 {i+1}. {title[:30]}\n"
            bookmark_text += f"   🔗 {display_url}\n"
            bookmark_text += f"   📅 {added[:10]}\n\n"
            
            # Add buttons for each bookmark
            keyboard.append([
                InlineKeyboardButton(f"🔖 {i+1}. {title[:15]}...", 
                                   callback_data=f"bookmark_clone_{url}")
            ])
        
        if len(bookmarks) > 10:
            bookmark_text += f"\n📄 {EXUFont.bold('Showing 10 of')} {len(bookmarks)} {EXUFont.bold('bookmarks')}\n"
        
        bookmark_text += f"\n{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}"
        
        # Add navigation buttons
        keyboard.append([InlineKeyboardButton("🔄 𝐑𝐞𝐟𝐫𝐞𝐬𝐡", callback_data="bookmarks")])
        keyboard.append([InlineKeyboardButton("◀️ 𝐁𝐚𝐜𝐤", callback_data="main_menu")])
        
        await query.edit_message_text(
            bookmark_text,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode=ParseMode.MARKDOWN
        )
    
    async def handle_bookmark_callback(self, query, data: str, user_id: int):
        """Handle bookmark-related callbacks"""
        if data.startswith("bookmark_"):
            action = data.replace("bookmark_", "", 1)
            
            if action.startswith("clone_"):
                url = action.replace("clone_", "", 1)
                # Start cloning this bookmark
                options = {
                    'strategy': 'smart',
                    'format': self.db.get_setting('default_format', 'zip')
                }
                await self.process_advanced_clone(query, url, user_id, options)
            
            elif action.startswith("delete_"):
                # Delete bookmark (to be implemented)
                await query.answer("🗑️ 𝐁𝐨𝐨𝐤𝐦𝐚𝐫𝐤 𝐝𝐞𝐥𝐞𝐭𝐢𝐨𝐧 𝐜𝐨𝐦𝐢𝐧𝐠 𝐬𝐨𝐨𝐧!", show_alert=True)
    
    async def show_user_settings(self, query):
        """Show user settings"""
        user_id = query.from_user.id
        settings = self.db.get_user_settings(user_id)
        
        settings_text = f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
        settings_text += f"⚙️ {EXUFont.bold('𝐘𝐎𝐔𝐑 𝐒𝐄𝐓𝐓𝐈𝐍𝐆𝐒')}\n"
        settings_text += f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n\n"
        
        # Current settings
        settings_text += f"🎨 {EXUFont.bold('𝐓𝐡𝐞𝐦𝐞:')} {settings.get('theme', 'dark').title()}\n"
        settings_text += f"🔔 {EXUFont.bold('𝐍𝐨𝐭𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧𝐬:')} {'✅ 𝐎𝐧' if settings.get('notifications', True) else '❌ 𝐎𝐟𝐟'}\n"
        settings_text += f"💾 {EXUFont.bold('𝐀𝐮𝐭𝐨-𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝:')} {'✅ 𝐎𝐧' if settings.get('auto_download', True) else '❌ 𝐎𝐟𝐟'}\n"
        settings_text += f"⭐ {EXUFont.bold('𝐐𝐮𝐚𝐥𝐢𝐭𝐲:')} {settings.get('quality', 'high').title()}\n"
        settings_text += f"📁 {EXUFont.bold('𝐅𝐨𝐫𝐦𝐚𝐭:')} {settings.get('format', 'zip').upper()}\n"
        
        settings_text += f"\n{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
        settings_text += f"⚡ {EXUFont.bold('𝐐𝐔𝐈𝐂𝐊 𝐒𝐄𝐓𝐓𝐈𝐍𝐆𝐒:')}\n"
        
        keyboard = [
            [
                InlineKeyboardButton("🎨 𝐓𝐡𝐞𝐦𝐞", callback_data="setting_theme"),
                InlineKeyboardButton("🔔 𝐍𝐨𝐭𝐢𝐟𝐲", callback_data="setting_notify")
            ],
            [
                InlineKeyboardButton("💾 𝐀𝐮𝐭𝐨-𝐝𝐥", callback_data="setting_auto"),
                InlineKeyboardButton("⭐ 𝐐𝐮𝐚𝐥𝐢𝐭𝐲", callback_data="setting_quality")
            ],
            [
                InlineKeyboardButton("📁 𝐅𝐨𝐫𝐦𝐚𝐭", callback_data="setting_format"),
                InlineKeyboardButton("🔄 𝐑𝐞𝐬𝐞𝐭", callback_data="setting_reset")
            ],
            [InlineKeyboardButton("◀️ 𝐁𝐚𝐜𝐤", callback_data="main_menu")]
        ]
        
        await query.edit_message_text(
            settings_text,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode=ParseMode.MARKDOWN
        )
    
    async def show_bot_status(self, query):
        """Show advanced bot status"""
        uptime = datetime.now() - self.start_time
        hours, remainder = divmod(int(uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        
        # Get advanced stats
        cursor = self.db.conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM users')
        total_users = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM clones WHERE status = "success"')
        total_clones = cursor.fetchone()[0]
        
        cursor.execute('SELECT SUM(size_mb) FROM clones WHERE status = "success"')
        total_storage = cursor.fetchone()[0] or 0
        
        cursor.execute('SELECT COUNT(*) FROM queue WHERE status = "processing"')
        active_batches = cursor.fetchone()[0]
        
        status_text = f"""
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
⚡ {EXUFont.bold('𝐄𝐗𝐔 𝐂𝐋𝐎𝐍𝐄𝐑 𝐏𝐑𝐎 - 𝐒𝐓𝐀𝐓𝐔𝐒')}
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}

🤖 {EXUFont.bold('𝐁𝐨𝐭:')} 𝐄𝐗𝐔 𝐂𝐥𝐨𝐧𝐞𝐫 𝐏𝐑𝐎 v6.0
⚡ {EXUFont.bold('𝐒𝐭𝐚𝐭𝐮𝐬:')} 🟢 𝐎𝐧𝐥𝐢𝐧𝐞
⏱️ {EXUFont.bold('𝐔𝐩𝐭𝐢𝐦𝐞:')} {hours}h {minutes}m {seconds}s
📅 {EXUFont.bold('𝐒𝐭𝐚𝐫𝐭𝐞𝐝:')} {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
💻 {EXUFont.bold('𝐒𝐘𝐒𝐓𝐄𝐌 𝐒𝐓𝐀𝐓𝐒:')}

💾 𝐌𝐞𝐦𝐨𝐫𝐲: {psutil.Process().memory_info().rss / 1024 / 1024:.1f} MB
⚡ 𝐂𝐏𝐔: {psutil.cpu_percent()}%
💿 𝐃𝐢𝐬𝐤: {psutil.disk_usage('.').percent}%

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
📊 {EXUFont.bold('𝐁𝐎𝐓 𝐒𝐓𝐀𝐓𝐈𝐒𝐓𝐈𝐂𝐒:')}

👥 𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫𝐬: {total_users}
🚀 𝐓𝐨𝐭𝐚𝐥 𝐂𝐥𝐨𝐧𝐞𝐬: {total_clones}
💾 𝐓𝐨𝐭𝐚𝐥 𝐒𝐭𝐨𝐫𝐚𝐠𝐞: {total_storage:.1f} MB
📦 𝐀𝐜𝐭𝐢𝐯𝐞 𝐁𝐚𝐭𝐜𝐡𝐞𝐬: {active_batches}
⚡ 𝐀𝐜𝐭𝐢𝐯𝐞 𝐂𝐥𝐨𝐧𝐞𝐬: {len(self.active_clones)}

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
⚙️ {EXUFont.bold('𝐒𝐄𝐓𝐓𝐈𝐍𝐆𝐒:')}

📢 𝐂𝐡𝐚𝐧𝐧𝐞𝐥: {Config.CHANNEL_USERNAME}
🛡️ 𝐕𝐞𝐫𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧: {'✅ 𝐎𝐧' if self.db.get_setting('force_join', '1') == '1' else '❌ 𝐎𝐟𝐟'}
📊 𝐃𝐚𝐢𝐥𝐲 𝐋𝐢𝐦𝐢𝐭: {self.db.get_setting('max_clones_per_day', '20')}
"""
        
        await query.edit_message_text(
            status_text,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔄 𝐑𝐞𝐟𝐫𝐞𝐬𝐡", callback_data="bot_status")],
                [InlineKeyboardButton("◀️ 𝐁𝐚𝐜𝐤", callback_data="main_menu")]
            ]),
            parse_mode=ParseMode.MARKDOWN
        )
    
    async def show_help(self, query):
        """Show advanced help information"""
        help_text = f"""
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
🆘 {EXUFont.bold('𝐀𝐃𝐕𝐀𝐍𝐂𝐄𝐃 𝐇𝐄𝐋𝐏 & 𝐒𝐔𝐏𝐏𝐎𝐑𝐓')}
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}

📚 {EXUFont.bold('𝐇𝐎𝐖 𝐓𝐎 𝐔𝐒𝐄 𝐄𝐗𝐔 𝐂𝐋𝐎𝐍𝐄𝐑 𝐏𝐑𝐎:')}

1. 𝐉𝐨𝐢𝐧 𝐭𝐡𝐞 𝐫𝐞𝐪𝐮𝐢𝐫𝐞𝐝 𝐜𝐡𝐚𝐧𝐧𝐞𝐥
2. 𝐕𝐞𝐫𝐢𝐟𝐲 𝐲𝐨𝐮𝐫 𝐦𝐞𝐦𝐛𝐞𝐫𝐬𝐡𝐢𝐩
3. 𝐂𝐥𝐢𝐜𝐤 "𝐂𝐥𝐨𝐧𝐞 𝐖𝐞𝐛𝐬𝐢𝐭𝐞"
4. 𝐒𝐞𝐥𝐞𝐜𝐭 𝐜𝐥𝐨𝐧𝐢𝐧𝐠 𝐬𝐭𝐫𝐚𝐭𝐞𝐠𝐲 𝐚𝐧𝐝 𝐟𝐨𝐫𝐦𝐚𝐭
5. 𝐒𝐞𝐧𝐝 𝐭𝐡𝐞 𝐔𝐑𝐋 𝐲𝐨𝐮 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐜𝐥𝐨𝐧𝐞
6. 𝐖𝐚𝐢𝐭 𝐟𝐨𝐫 𝐩𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠
7. 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐭𝐡𝐞 𝐫𝐞𝐬𝐮𝐥𝐭

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
⚡ {EXUFont.bold('𝐂𝐋𝐎𝐍𝐈𝐍𝐆 𝐒𝐓𝐑𝐀𝐓𝐄𝐆𝐈𝐄𝐒:')}

🔍 {EXUFont.bold('𝐁𝐚𝐬𝐢𝐜:')} 𝐒𝐢𝐦𝐩𝐥𝐞 𝐇𝐓𝐌𝐋/𝐂𝐒𝐒/𝐉𝐒 𝐜𝐥𝐨𝐧𝐢𝐧𝐠
⚡ {EXUFont.bold('𝐃𝐞𝐞𝐩:')} 𝐌𝐮𝐥𝐭𝐢-𝐩𝐚𝐠𝐞 𝐜𝐥𝐨𝐧𝐢𝐧𝐠 𝐰𝐢𝐭𝐡 𝐥𝐢𝐧𝐤 𝐟𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠
🤖 {EXUFont.bold('𝐒𝐦𝐚𝐫𝐭:')} 𝐀𝐮𝐭𝐨-𝐝𝐞𝐭𝐞𝐜𝐭 𝐛𝐞𝐬𝐭 𝐬𝐭𝐫𝐚𝐭𝐞𝐠𝐲

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
📁 {EXUFont.bold('𝐎𝐔𝐓𝐏𝐔𝐓 𝐅𝐎𝐑𝐌𝐀𝐓𝐒:')}

📁 {EXUFont.bold('𝐙𝐈𝐏:')} 𝐂𝐨𝐦𝐩𝐫𝐞𝐬𝐬𝐞𝐝 𝐚𝐫𝐜𝐡𝐢𝐯𝐞
📦 {EXUFont.bold('𝐓𝐀𝐑.𝐆𝐙:')} 𝐔𝐧𝐢𝐱-𝐬𝐭𝐲𝐥𝐞 𝐚𝐫𝐜𝐡𝐢𝐯𝐞
🌐 {EXUFont.bold('𝐒𝐢𝐧𝐠𝐥𝐞 𝐇𝐓𝐌𝐋:')} 𝐀𝐥𝐥 𝐢𝐧 𝐨𝐧𝐞 𝐟𝐢𝐥𝐞

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
🔧 {EXUFont.bold('𝐓𝐑𝐎𝐔𝐁𝐋𝐄𝐒𝐇𝐎𝐎𝐓𝐈𝐍𝐆:')}

❌ {EXUFont.bold('𝐂𝐚𝐧')}𝐭 𝐜𝐥𝐨𝐧𝐞: 𝐓𝐫𝐲 𝐛𝐚𝐬𝐢𝐜 𝐬𝐭𝐫𝐚𝐭𝐞𝐠𝐲 𝐨𝐫 𝐬𝐢𝐦𝐩𝐥𝐞𝐫 𝐬𝐢𝐭𝐞𝐬
⏳ {EXUFont.bold('𝐓𝐢𝐦𝐞𝐨𝐮𝐭:')} 𝐂𝐡𝐞𝐜𝐤 𝐢𝐧𝐭𝐞𝐫𝐧𝐞𝐭 𝐜𝐨𝐧𝐧𝐞𝐜𝐭𝐢𝐨𝐧
💾 {EXUFont.bold('𝐍𝐨 𝐬𝐭𝐨𝐫𝐚𝐠𝐞:')} 𝐂𝐥𝐞𝐚𝐧 𝐨𝐥𝐝 𝐜𝐥𝐨𝐧𝐞𝐬
🐛 {EXUFont.bold('𝐁𝐮𝐠𝐬:')} 𝐑𝐞𝐩𝐨𝐫𝐭 𝐭𝐨 𝐬𝐮𝐩𝐩𝐨𝐫𝐭

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
💬 {EXUFont.bold('𝐒𝐔𝐏𝐏𝐎𝐑𝐓:')}

𝐅𝐨𝐫 𝐬𝐮𝐩𝐩𝐨𝐫𝐭, 𝐪𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬, 𝐨𝐫 𝐟𝐞𝐞𝐝𝐛𝐚𝐜𝐤:
{Config.SUPPORT_GROUP}

📢 {EXUFont.bold('𝐔𝐩𝐝𝐚𝐭𝐞𝐬 & 𝐀𝐧𝐧𝐨𝐮𝐧𝐜𝐞𝐦𝐞𝐧𝐭𝐬:')}
{Config.CHANNEL_USERNAME}
"""
        
        await query.edit_message_text(
            help_text,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("◀️ 𝐁𝐚𝐜𝐤", callback_data="main_menu")]
            ]),
            parse_mode=ParseMode.MARKDOWN
        )
    
    # ==============================================
    # 𝐀𝐃𝐕𝐀𝐍𝐂𝐄𝐃 𝐀𝐃𝐌𝐈𝐍 𝐅𝐄𝐀𝐓𝐔𝐑𝐄𝐒
    # ==============================================
    
    async def show_admin_panel(self, query, user_id: int):
        """Show advanced admin panel"""
        if user_id not in Config.ADMIN_IDS:
            await query.answer("❌ 𝐀𝐜𝐜𝐞𝐬𝐬 𝐝𝐞𝐧𝐢𝐞𝐝!", show_alert=True)
            await self.show_main_menu(query)
            return
        
        admin_text = f"""
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
👑 {EXUFont.bold('𝐀𝐃𝐕𝐀𝐍𝐂𝐄𝐃 𝐀𝐃𝐌𝐈𝐍 𝐏𝐀𝐍𝐄𝐋')}
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}

⚡ {EXUFont.bold('𝐖𝐞𝐥𝐜𝐨𝐦𝐞, 𝐀𝐝𝐦𝐢𝐧!')}

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
📊 {EXUFont.bold('𝐐𝐔𝐈𝐂𝐊 𝐒𝐓𝐀𝐓𝐒:')}

• 𝐁𝐨𝐭 𝐔𝐩𝐭𝐢𝐦𝐞: {(datetime.now() - self.start_time).total_seconds() / 3600:.1f}𝐡
• 𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫𝐬: {self.db.conn.execute('SELECT COUNT(*) FROM users').fetchone()[0]}
• 𝐀𝐜𝐭𝐢𝐯𝐞 𝐂𝐥𝐨𝐧𝐞𝐬: {len(self.active_clones)}
• 𝐓𝐨𝐝𝐚𝐲'𝐬 𝐂𝐥𝐨𝐧𝐞𝐬: {self.get_today_clones()}

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
⚡ {EXUFont.bold('𝐀𝐃𝐌𝐈𝐍 𝐓𝐎𝐎𝐋𝐒:')}

👥 {EXUFont.bold('𝐔𝐬𝐞𝐫 𝐌𝐚𝐧𝐚𝐠𝐞𝐦𝐞𝐧𝐭')} - 𝐌𝐚𝐧𝐚𝐠𝐞 𝐮𝐬𝐞𝐫𝐬 & 𝐩𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧𝐬
📊 {EXUFont.bold('𝐀𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐒𝐭𝐚𝐭𝐬')} - 𝐃𝐞𝐭𝐚𝐢𝐥𝐞𝐝 𝐬𝐭𝐚𝐭𝐬 & 𝐫𝐞𝐩𝐨𝐫𝐭𝐬
⚙️ {EXUFont.bold('𝐁𝐨𝐭 𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬')} - 𝐂𝐨𝐧𝐟𝐢𝐠𝐮𝐫𝐞 𝐛𝐨𝐭 𝐬𝐞𝐭𝐭𝐢𝐧𝐠𝐬
📢 {EXUFont.bold('𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭')} - 𝐒𝐞𝐧𝐝 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬 𝐭𝐨 𝐚𝐥𝐥 𝐮𝐬𝐞𝐫𝐬
🧹 {EXUFont.bold('𝐂𝐥𝐞𝐚𝐧𝐮𝐩')} - 𝐂𝐥𝐞𝐚𝐧 𝐭𝐞𝐦𝐩 𝐟𝐢𝐥𝐞𝐬 𝐚𝐧𝐝 𝐜𝐚𝐜𝐡𝐞

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
⚡ {EXUFont.bold('𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒:')}

/admin - 𝐎𝐩𝐞𝐧 𝐚𝐝𝐦𝐢𝐧 𝐩𝐚𝐧𝐞𝐥
/stats - 𝐒𝐡𝐨𝐰 𝐝𝐞𝐭𝐚𝐢𝐥𝐞𝐝 𝐬𝐭𝐚𝐭𝐬
/users - 𝐋𝐢𝐬𝐭 𝐚𝐥𝐥 𝐮𝐬𝐞𝐫𝐬
/broadcast - 𝐒𝐞𝐧𝐝 𝐦𝐞𝐬𝐚𝐠𝐞 𝐭𝐨 𝐚𝐥𝐥
/cleanup - 𝐂𝐥𝐞𝐚𝐧 𝐭𝐞𝐦𝐩 𝐟𝐢𝐥𝐞𝐬
"""
        
        await query.edit_message_text(
            admin_text,
            reply_markup=self.admin_menu(),
            parse_mode=ParseMode.MARKDOWN
        )
    
    async def handle_admin_callback(self, query, context: CallbackContext, data: str, user_id: int):
        """Handle advanced admin callbacks"""
        if user_id not in Config.ADMIN_IDS:
            await query.answer("❌ 𝐀𝐜𝐜𝐞𝐬𝐬 𝐝𝐞𝐧𝐢𝐞𝐝!", show_alert=True)
            return
        
        handlers = {
            "admin_users": self.show_user_management,
            "admin_stats": self.show_admin_stats,
            "admin_settings": self.show_admin_settings,
            "admin_broadcast": self.start_broadcast,
            "admin_cleanup": self.admin_cleanup
        }
        
        if data in handlers:
            await handlers[data](query)
        else:
            await query.answer("⚡ 𝐅𝐞𝐚𝐭𝐮𝐫𝐞 𝐜𝐨𝐦𝐢𝐧𝐠 𝐬𝐨𝐨𝐧!", show_alert=True)
    
    async def admin_cleanup(self, query):
        """Admin cleanup tool"""
        # Clean temp directories
        temp_dirs = []
        for item in os.listdir(tempfile.gettempdir()):
            if item.startswith("exu_pro_clone_"):
                temp_dirs.append(os.path.join(tempfile.gettempdir(), item))
        
        cleaned = 0
        for temp_dir in temp_dirs:
            try:
                shutil.rmtree(temp_dir)
                cleaned += 1
            except:
                pass
        
        await query.edit_message_text(
            f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
            f"🧹 {EXUFont.bold('𝐂𝐋𝐄𝐀𝐍𝐔𝐏 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄')}\n"
            f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n\n"
            f"✅ {EXUFont.bold('𝐑𝐞𝐬𝐮𝐥𝐭𝐬:')}\n"
            f"• 𝐓𝐞𝐦𝐩 𝐝𝐢𝐫𝐞𝐜𝐭𝐨𝐫𝐢𝐞𝐬 𝐜𝐥𝐞𝐚𝐧𝐞𝐝: {cleaned}\n\n"
            f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
            f"⚡ {EXUFont.bold('𝐒𝐲𝐬𝐭𝐞𝐦 𝐨𝐩𝐭𝐢𝐦𝐢𝐳𝐞𝐝!')}",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("◀️ 𝐁𝐚𝐜𝐤", callback_data="admin_panel")]
            ]),
            parse_mode=ParseMode.MARKDOWN
        )
    
    async def show_admin_stats(self, query):
        """Show admin statistics"""
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

📅 {EXUFont.bold('𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝:')} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

📊 {EXUFont.bold('𝐁𝐎𝐓 𝐒𝐓𝐀𝐓𝐒:')}
• 𝐔𝐩𝐭𝐢𝐦𝐞: {hours}h {minutes}m {seconds}s
• 𝐌𝐞𝐦𝐨𝐫𝐲: {psutil.Process().memory_info().rss / 1024 / 1024:.1f} MB
• 𝐂𝐏𝐔: {psutil.cpu_percent()}%
• 𝐃𝐢𝐬𝐤: {psutil.disk_usage('.').percent}%

👥 {EXUFont.bold('𝐔𝐒𝐄𝐑 𝐒𝐓𝐀𝐓𝐒:')}
• 𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫𝐬: {total_users}
• 𝐕𝐞𝐫𝐢𝐟𝐢𝐞𝐝: {self.db.conn.execute('SELECT COUNT(*) FROM users WHERE is_verified = 1').fetchone()[0]}
• 𝐁𝐚𝐧𝐧𝐞𝐝: {self.db.conn.execute('SELECT COUNT(*) FROM users WHERE is_banned = 1').fetchone()[0]}
• 𝐀𝐜𝐭𝐢𝐯𝐞 (𝟐𝟒𝐡): {self.get_active_users_24h()}

🚀 {EXUFont.bold('𝐂𝐋𝐎𝐍𝐄 𝐒𝐓𝐀𝐓𝐒:')}
• 𝐓𝐨𝐭𝐚𝐥 𝐂𝐥𝐨𝐧𝐞𝐬: {total_clones}
• 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥: {success_clones}
• 𝐒𝐮𝐜𝐜𝐞𝐬𝐬 𝐑𝐚𝐭𝐞: {(success_clones / max(total_clones, 1) * 100):.1f}%
• 𝐓𝐨𝐭𝐚𝐥 𝐒𝐭𝐨𝐫𝐚𝐠𝐞: {total_storage:.2f} MB
• 𝐓𝐨𝐝𝐚𝐲'𝐬 𝐂𝐥𝐨𝐧𝐞𝐬: {self.get_today_clones()}
"""
        
        await query.edit_message_text(
            stats_text,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔄 𝐑𝐞𝐟𝐫𝐞𝐬𝐡", callback_data="admin_stats")],
                [InlineKeyboardButton("◀️ 𝐁𝐚𝐜𝐤", callback_data="admin_panel")]
            ]),
            parse_mode=ParseMode.MARKDOWN
        )
    
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
    
    async def show_admin_settings(self, query):
        """Show admin settings"""
        settings_text = f"""
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐁𝐎𝐓 𝐒𝐄𝐓𝐓𝐈𝐍𝐆𝐒')}
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}

⚙️ {EXUFont.bold('𝐂𝐔𝐑𝐑𝐄𝐍𝐓 𝐒𝐄𝐓𝐓𝐈𝐍𝐆𝐒:')}

• 𝐂𝐡𝐚𝐧𝐧𝐞𝐥: {Config.CHANNEL_USERNAME}
• 𝐅𝐨𝐫𝐜𝐞 𝐉𝐨𝐢𝐧: {'✅ 𝐎𝐧' if self.db.get_setting('force_join', '1') == '1' else '❌ 𝐎𝐟𝐟'}
• 𝐃𝐚𝐢𝐥𝐲 𝐂𝐥𝐨𝐧𝐞 𝐋𝐢𝐦𝐢𝐭: {self.db.get_setting('max_clones_per_day', '20')}
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

📢 {EXUFont.bold('𝐒𝐞𝐧𝐝 𝐚 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐭𝐨 𝐚𝐥𝐥 𝐮𝐬𝐞𝐫𝐬:')}

𝐔𝐬𝐚𝐠𝐞:
/broadcast 𝐘𝐨𝐮𝐫 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐡𝐞𝐫𝐞

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
{EXUFont.bold('𝐄𝐱𝐚𝐦𝐩𝐥𝐞:')}
/broadcast 𝐁𝐨𝐭 𝐰𝐢𝐥𝐥 𝐛𝐞 𝐝𝐨𝐰𝐧 𝐟𝐨𝐫 𝐦𝐚𝐢𝐧𝐭𝐞𝐧𝐚𝐧𝐜𝐞 𝐭𝐨𝐦𝐨𝐫𝐫𝐨𝐰
"""
        
        await query.edit_message_text(
            broadcast_text,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("◀️ 𝐁𝐚𝐜𝐤", callback_data="admin_panel")]
            ]),
            parse_mode=ParseMode.MARKDOWN
        )
    
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
        elif command == "/cleanup":
            await self.cleanup_command(update)
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
                "/setchannel @user - 𝐒𝐞𝐭 𝐜𝐡𝐚𝐧𝐧𝐞𝐥\n"
                "/cleanup - 𝐂𝐥𝐞𝐚𝐧 𝐭𝐞𝐦𝐩 𝐟𝐢𝐥𝐞𝐬",
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

📅 {EXUFont.bold('𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝:')} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

📊 {EXUFont.bold('𝐁𝐎𝐓 𝐒𝐓𝐀𝐓𝐒:')}
• 𝐔𝐩𝐭𝐢𝐦𝐞: {hours}h {minutes}m {seconds}s
• 𝐌𝐞𝐦𝐨𝐫𝐲: {psutil.Process().memory_info().rss / 1024 / 1024:.1f} MB
• 𝐂𝐏𝐔: {psutil.cpu_percent()}%
• 𝐃𝐢𝐬𝐤: {psutil.disk_usage('.').percent}%

👥 {EXUFont.bold('𝐔𝐒𝐄𝐑 𝐒𝐓𝐀𝐓𝐒:')}
• 𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫𝐬: {total_users}
• 𝐕𝐞𝐫𝐢𝐟𝐢𝐞𝐝: {self.db.conn.execute('SELECT COUNT(*) FROM users WHERE is_verified = 1').fetchone()[0]}
• 𝐁𝐚𝐧𝐧𝐞𝐝: {self.db.conn.execute('SELECT COUNT(*) FROM users WHERE is_banned = 1').fetchone()[0]}
• 𝐀𝐜𝐭𝐢𝐯𝐞 (𝟐𝟒𝐡): {self.get_active_users_24h()}

🚀 {EXUFont.bold('𝐂𝐋𝐎𝐍𝐄 𝐒𝐓𝐀𝐓𝐒:')}
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
- 𝐄𝐗𝐔 𝐂𝐥𝐨𝐧𝐞𝐫 𝐏𝐑𝐎 𝐓𝐞𝐚𝐦
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

👤 {EXUFont.bold('𝐍𝐚𝐦𝐞:')} {name}
📛 {EXUFont.bold('𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞:')} @{username or 'N/A'}
🆔 {EXUFont.bold('𝐔𝐬𝐞𝐫 𝐈𝐃:')} {user_id}
📅 {EXUFont.bold('𝐉𝐨𝐢𝐧𝐞𝐝:')} {join_date}
🕒 {EXUFont.bold('𝐋𝐚𝐬𝐭 𝐀𝐜𝐭𝐢𝐯𝐞:')} {last_active}
🛡️ {EXUFont.bold('𝐒𝐭𝐚𝐭𝐮𝐬:')} {'✅ 𝐕𝐞𝐫𝐢𝐟𝐢𝐞𝐝' if verified else '⭕ 𝐏𝐞𝐧𝐝𝐢𝐧𝐠'}
🚫 {EXUFont.bold('𝐁𝐚𝐧𝐧𝐞𝐝:')} {'✅ 𝐘𝐞𝐬' if banned else '❌ 𝐍𝐨'}

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
📊 {EXUFont.bold('𝐒𝐓𝐀𝐓𝐈𝐒𝐓𝐈𝐂𝐒:')}

• 𝐓𝐨𝐭𝐚𝐥 𝐂𝐥𝐨𝐧𝐞𝐬: {total_clones}
• 𝐂𝐥𝐨𝐧𝐞𝐬 𝐓𝐨𝐝𝐚𝐲: {clones_today}/{self.db.get_setting('max_clones_per_day', '20')}

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
👑 {EXUFont.bold('𝐀𝐃𝐌𝐈𝐍 𝐀𝐂𝐓𝐈𝐎𝐍𝐒:')}

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
    
    async def cleanup_command(self, update: Update):
        """Cleanup command"""
        # Clean temp directories
        temp_dirs = []
        for item in os.listdir(tempfile.gettempdir()):
            if item.startswith("exu_pro_clone_"):
                temp_dirs.append(os.path.join(tempfile.gettempdir(), item))
        
        cleaned = 0
        for temp_dir in temp_dirs:
            try:
                shutil.rmtree(temp_dir)
                cleaned += 1
            except:
                pass
        
        await update.message.reply_text(f"✅ 𝐂𝐥𝐞𝐚𝐧𝐞𝐝 {cleaned} 𝐭𝐞𝐦𝐩𝐨𝐫𝐚𝐫𝐲 𝐝𝐢𝐫𝐞𝐜𝐭𝐨𝐫𝐢𝐞𝐬.")
    
    # ==============================================
    # 𝐔𝐓𝐈𝐋𝐈𝐓𝐘 𝐌𝐄𝐓𝐇𝐎𝐃𝐒
    # ==============================================
    
    def get_today_clones(self) -> int:
        """Get number of clones today"""
        cursor = self.db.conn.cursor()
        today = datetime.now().date().isoformat()
        cursor.execute('SELECT COUNT(*) FROM clones WHERE timestamp LIKE ?', (f'{today}%',))
        return cursor.fetchone()[0]
    
    def get_active_users_24h(self) -> int:
        """Get number of active users in last 24 hours"""
        cursor = self.db.conn.cursor()
        twenty_four_hours_ago = (datetime.now() - timedelta(hours=24)).isoformat()
        cursor.execute('SELECT COUNT(*) FROM users WHERE last_active > ?', (twenty_four_hours_ago,))
        return cursor.fetchone()[0]
    
    async def verify_user(self, query, context: CallbackContext):
        """Verify user has joined channel"""
        user_id = query.from_user.id
        
        # Show checking animation
        await query.edit_message_text(
            f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
            f"🛡️ {EXUFont.bold('𝐂𝐇𝐄𝐂𝐊𝐈𝐍𝐆 𝐌𝐄𝐌𝐁𝐄𝐑𝐒𝐇𝐈𝐏')}\n"
            f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n\n"
            f"⚡ {EXUFont.bold('𝐏𝐥𝐞𝐚𝐬𝐞 𝐰𝐚𝐢𝐭, 𝐜𝐡𝐞𝐜𝐤𝐢𝐧𝐠...')}\n\n"
            f"{EXUFont.create_progress(0.3)}",
            parse_mode=ParseMode.MARKDOWN
        )
        
        # Check membership
        try:
            chat_member = await context.bot.get_chat_member(
                Config.CHANNEL_USERNAME, 
                user_id
            )
            is_member = chat_member.status in ['member', 'administrator', 'creator']
        except:
            is_member = False
        
        if is_member:
            # Mark as verified
            self.db.verify_user(user_id)
            
            await query.edit_message_text(
                f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
                f"✅ {EXUFont.bold('𝐕𝐄𝐑𝐈𝐅𝐈𝐂𝐀𝐓𝐈𝐎𝐍 𝐒𝐔𝐂𝐂𝐄𝐒𝐒!')}\n"
                f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n\n"
                f"🎉 {EXUFont.bold('𝐓𝐡𝐚𝐧𝐤 𝐲𝐨𝐮 𝐟𝐨𝐫 𝐣𝐨𝐢𝐧𝐢𝐧𝐠!')}\n\n"
                f"𝐘𝐨𝐮 𝐧𝐨𝐰 𝐡𝐚𝐯𝐞 𝐟𝐮𝐥𝐥 𝐚𝐜𝐜𝐞𝐬𝐬 𝐭𝐨 𝐄𝐗𝐔 𝐂𝐥𝐨𝐧𝐞𝐫 𝐏𝐑𝐎.\n\n"
                f"✨ {EXUFont.bold('𝐁𝐨𝐧𝐮𝐬:')} 𝐑𝐞𝐜𝐞𝐢𝐯𝐞𝐝 𝟓𝟎 𝐜𝐫𝐞𝐝𝐢𝐭𝐬 𝐟𝐨𝐫 𝐣𝐨𝐢𝐧𝐢𝐧𝐠!",
                reply_markup=self.main_menu(user_id),
                parse_mode=ParseMode.MARKDOWN
            )
        else:
            # Show join message again
            join_msg, keyboard = self.get_join_message()
            await query.edit_message_text(
                f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n"
                f"❌ {EXUFont.bold('𝐕𝐄𝐑𝐈𝐅𝐈𝐂𝐀𝐓𝐈𝐎𝐍 𝐅𝐀𝐈𝐋𝐄𝐃')}\n"
                f"{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}\n\n"
                f"⚠️ {EXUFont.bold('𝐏𝐥𝐞𝐚𝐬𝐞 𝐣𝐨𝐢𝐧 𝐭𝐡𝐞 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐟𝐢𝐫𝐬𝐭.')}\n\n"
                f"𝐂𝐥𝐢𝐜𝐤 𝐭𝐡𝐞 𝐛𝐮𝐭𝐭𝐨𝐧𝐬 𝐛𝐞𝐥𝐨𝐰 𝐭𝐨 𝐣𝐨𝐢𝐧 𝐚𝐧𝐝 𝐭𝐫𝐲 𝐚𝐠𝐚𝐢𝐧.",
                reply_markup=keyboard,
                parse_mode=ParseMode.MARKDOWN
            )
    
    async def show_main_menu(self, query):
        """Show main menu"""
        user_id = query.from_user.id
        user_stats = self.db.get_user_stats_advanced(user_id)
        
        menu_text = f"""
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
⚡ {EXUFont.bold('𝐄𝐗𝐔 𝐂𝐋𝐎𝐍𝐄𝐑 𝐏𝐑𝐎 𝐌𝐄𝐍𝐔')}
{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}

👤 {EXUFont.bold('𝐔𝐬𝐞𝐫:')} {user_stats.get('name', 'User')}
⭐ {EXUFont.bold('𝐋𝐞𝐯𝐞𝐥:')} {user_stats.get('level', 1)}
📊 {EXUFont.bold('𝐂𝐥𝐨𝐧𝐞𝐬 𝐓𝐨𝐝𝐚𝐲:')} {user_stats.get('clones_today', 0)}/{self.db.get_setting('max_clones_per_day', '20')}
🏆 {EXUFont.bold('𝐓𝐨𝐭𝐚𝐥 𝐂𝐥𝐨𝐧𝐞𝐬:')} {user_stats.get('total_clones', 0)}

{EXUFont.bold('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')}
🎯 {EXUFont.bold('𝐒𝐄𝐋𝐄𝐂𝐓 𝐀𝐍 𝐎𝐏𝐓𝐈𝐎𝐍:')}
"""
        
        await query.edit_message_text(
            menu_text,
            reply_markup=self.main_menu(user_id),
            parse_mode=ParseMode.MARKDOWN
        )
    
    # ==============================================
    # 𝐁𝐎𝐓 𝐒𝐄𝐓𝐔𝐏 & 𝐑𝐔𝐍
    # ==============================================
    
    async def run(self):
        """Run the advanced bot"""
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
        self.app.add_handler(CommandHandler("cleanup", self.handle_admin_command))
        
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
        print(EXUFont.banner())
        print(EXUFont.log("🚀", "SYSTEM", "EXU Cloner PRO v6.0 Started", "SUCCESS"))
        print(EXUFont.log("⚡", "SYSTEM", f"Bot Token: {'*' * len(Config.TOKEN)}", "INFO"))
        print(EXUFont.log("👑", "ADMIN", f"Admin IDs: {Config.ADMIN_IDS}", "INFO"))
        print(EXUFont.log("📢", "CHANNEL", f"Channel: {Config.CHANNEL_USERNAME}", "INFO"))
        print(EXUFont.log("🤖", "SYSTEM", "Advanced features enabled:", "INFO"))
        print(EXUFont.log("  ", "FEATURES", "• Deep cloning with multi-page support", "INFO"))
        print(EXUFont.log("  ", "FEATURES", "• Multiple output formats (ZIP, TAR, HTML)", "INFO"))
        print(EXUFont.log("  ", "FEATURES", "• Batch processing queue system", "INFO"))
        print(EXUFont.log("  ", "FEATURES", "• User bookmarks and settings", "INFO"))
        print(EXUFont.log("  ", "FEATURES", "• Quality scoring system", "INFO"))
        print(EXUFont.log("⚡", "SYSTEM", "Bot is now running...", "INFO"))
        
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
        bot = EXUClonerProBot()
        await bot.run()
    except KeyboardInterrupt:
        print("\n" + EXUFont.log("⚠️", "SYSTEM", "Bot shutdown requested", "WARNING"))
    except Exception as e:
        print(EXUFont.log("❌", "SYSTEM", f"Fatal error: {str(e)}", "ERROR"))
        import traceback
        traceback.print_exc()
    finally:
        print(EXUFont.log("🤖", "SYSTEM", "EXU Cloner PRO stopped", "INFO"))

if __name__ == "__main__":
    asyncio.run(main())
