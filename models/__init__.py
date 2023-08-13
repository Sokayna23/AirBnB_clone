#!/usr/bin/python3
"""
Initializing package
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
