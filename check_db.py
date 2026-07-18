import sqlite3

DB_PATH = "data/bot.db"

print("🔍 Проверка базы данных...")

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Проверяем таблицы
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cur.fetchall()
print("📋 Таблицы в базе:", [t[0] for t in tables])

# Проверяем факты
if 'facts' in [t[0] for t in tables]:
    cur.execute("SELECT COUNT(*) FROM facts")
    count = cur.fetchone()[0]
    print(f"📚 Фактов в базе: {count}")
    
    cur.execute("SELECT keyword, definition FROM facts LIMIT 5")
    facts = cur.fetchall()
    print("📝 Примеры фактов:")
    for keyword, definition in facts:
        print(f"  • {keyword}: {definition[:50]}...")
else:
    print("❌ Таблица 'facts' отсутствует!")

conn.close()