"""Zpětná kompatibilita — spustí CIVOP školení."""
import sys
sys.argv = [sys.argv[0], "civop"]
exec(open("run.py").read())
