import tkinter as tk
from tkinter import ttk

def create_club():
    # هنا يمكنك إضافة الكود الذي يتعامل مع إنشاء النادي
    pass

# إنشاء نافذة التطبيق
app = tk.Tk()
app.title('أنشئ ناديك وقارنة')

# إضافة حقول الإدخال
tk.Label(app, text='اسم النادي').pack(pady=(10, 0))
club_name_entry = ttk.Entry(app)
club_name_entry.pack(pady=(0, 10))

tk.Label(app, text='وصف النادي').pack()
club_description_entry = ttk.Entry(app)
club_description_entry.pack(pady=10)

tk.Label(app, text='موضوعات النادي').pack()
club_location_entry = ttk.Entry(app)
club_location_entry.pack(pady=(0, 20))

# إضافة زر الإنشاء
create_button = ttk.Button(app, text='إنشاء', command=create_club)
create_button.pack(pady=(0, 20))

# البدء بتشغيل الواجهة
app.mainloop()

