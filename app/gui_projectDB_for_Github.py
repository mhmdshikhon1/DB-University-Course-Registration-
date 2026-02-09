import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error


class ModernUniversityRegistrationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("🎓 نظام التسجيل الجامعي - University Course Registration System")
        self.root.geometry("1300x750")
        self.root.configure(bg='#2c3e50')

        # الألوان الرئيسية
        self.colors = {
            'primary': '#3498db',
            'secondary': '#2ecc71',
            'accent': '#e74c3c',
            'background': '#ecf0f1',
            'dark_bg': '#2c3e50',
            'text_light': '#f8f9fa',  # اللون الأساسي للنصوص الفاتحة
            'text_dark': '#212529',  # اللون الأساسي للنصوص الداكنة
            'success': '#27ae60',
            'warning': '#f39c12',
            'error': '#e74c3c',
        }

        # تنسيق الأنماط
        self.setup_styles()

        # اتصال بقاعدة البيانات
        self.db_connection = self.connect_to_database()

        # إنشاء واجهة المستخدم
        self.create_gui()

    def setup_styles(self):
        """إعداد أنماط التصميم"""
        style = ttk.Style()

        # تخصيص الأنماط
        style.configure('Primary.TButton',
                        background=self.colors['primary'],
                        foreground=self.colors['text_dark'],
                        padding=(10, 5),
                        font=('Arial', 10, 'bold'))

        style.configure('Success.TButton',
                        background=self.colors['success'],
                        foreground=self.colors['text_dark'],
                        padding=(10, 5),
                        font=('Arial', 10, 'bold'))

        style.configure('Warning.TButton',
                        background=self.colors['warning'],
                        foreground=self.colors['text_dark'],
                        padding=(10, 5),
                        font=('Arial', 10, 'bold'))

        style.configure('Error.TButton',
                        background=self.colors['error'],
                        foreground=self.colors['text_dark'],
                        padding=(10, 5),
                        font=('Arial', 10, 'bold'))

        style.configure('Header.TLabel',
                        background=self.colors['dark_bg'],
                        foreground=self.colors['text_dark'],
                        font=('Arial', 16, 'bold'),
                        padding=10)

        style.configure('Custom.Treeview',
                        background=self.colors['background'],
                        fieldbackground=self.colors['background'],
                        foreground=self.colors['text_dark'],
                        rowheight=25)

        style.configure('Custom.Treeview.Heading',
                        background=self.colors['primary'],
                        foreground=self.colors['text_dark'],
                        font=('Arial', 11, 'bold'))

    def connect_to_database(self):
        """الاتصال بقاعدة البيانات"""
        try:
            connection = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='حط الباسورد هنا',
                database='University_Course_Registration'
            )
            messagebox.showinfo("✅ نجاح", "تم الاتصال بقاعدة البيانات بنجاح!")
            return connection
        except Error as e:
            messagebox.showerror("❌ خطأ", f"فشل في الاتصال بقاعدة البيانات: {e}")
            return None

    def create_gui(self):
        """إنشاء واجهة المستخدم الرئيسية"""
        # رأس التطبيق
        self.create_header()

        # إنشاء تبويبات
        tab_control = ttk.Notebook(self.root)
        tab_control.pack(expand=1, fill='both', padx=10, pady=10)

        # تبويب الطلاب
        self.student_tab = ttk.Frame(tab_control)
        tab_control.add(self.student_tab, text='👥 إدارة الطلاب')

        # تبويب المقررات
        self.course_tab = ttk.Frame(tab_control)
        tab_control.add(self.course_tab, text='📚 إدارة المقررات')

        # تبويب التسجيل
        self.enrollment_tab = ttk.Frame(tab_control)
        tab_control.add(self.enrollment_tab, text='🎯 التسجيل في المقررات')

        # تبويب التقارير
        self.reports_tab = ttk.Frame(tab_control)
        tab_control.add(self.reports_tab, text='📊 التقارير والإحصائيات')

        # إنشاء محتوى كل تبويب
        self.create_student_tab()
        self.create_course_tab()
        self.create_enrollment_tab()
        self.create_reports_tab()

    def create_header(self):
        """إنشاء رأس التطبيق"""
        header_frame = tk.Frame(self.root, bg=self.colors['dark_bg'], height=80)
        header_frame.pack(fill='x', padx=10, pady=5)
        header_frame.pack_propagate(False)

        title_label = tk.Label(header_frame,
                               text="🎓 نظام التسجيل الجامعي - University Course Registration System",
                               bg=self.colors['dark_bg'],
                               fg=self.colors['text_light'],
                               font=('Arial', 18, 'bold'))
        title_label.pack(expand=True)

        # إضافة بعض الإحصائيات السريعة في الرأس
        stats_frame = tk.Frame(header_frame, bg=self.colors['dark_bg'])
        stats_frame.pack(side='right', padx=20)

        # يمكن إضافة إحصائيات حية هنا لاحقاً

    def create_student_tab(self):
        """إنشاء تبويب إدارة الطلاب"""
        # إطار البحث
        search_frame = tk.LabelFrame(self.student_tab, text="🔍 بحث الطلاب",
                                     bg=self.colors['background'],
                                     fg=self.colors['text_dark'],
                                     font=('Arial', 12, 'bold'),
                                     padx=10, pady=10)
        search_frame.pack(fill='x', padx=15, pady=10)

        tk.Label(search_frame, text="بحث بالاسم:",
                 bg=self.colors['background'],
                 font=('Arial', 10)).grid(row=0, column=0, padx=5, pady=5)

        self.student_search_entry = ttk.Entry(search_frame, width=30, font=('Arial', 10))
        self.student_search_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Button(search_frame, text="🔍 بحث",
                   command=self.search_students,
                   style='Primary.TButton').grid(row=0, column=2, padx=5, pady=5)

        ttk.Button(search_frame, text="🔄 عرض الكل",
                   command=self.display_all_students,
                   style='Success.TButton').grid(row=0, column=3, padx=5, pady=5)

        # جدول الطلاب
        table_frame = tk.Frame(self.student_tab, bg=self.colors['background'])
        table_frame.pack(fill='both', expand=True, padx=15, pady=10)

        columns = ('SID', 'SSN', 'FName', 'MName', 'LName', 'Level', 'Department', 'Phone', 'Email')
        self.student_tree = ttk.Treeview(table_frame, columns=columns, show='headings', height=15,
                                         style='Custom.Treeview')

        # تعريف العناوين مع ألوان
        for col in columns:
            self.student_tree.heading(col, text=col)
            self.student_tree.column(col, width=100)

        # شريط التمرير
        scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=self.student_tree.yview)
        self.student_tree.configure(yscrollcommand=scrollbar.set)

        self.student_tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        # أزرار التحكم
        control_frame = tk.Frame(self.student_tab, bg=self.colors['background'])
        control_frame.pack(fill='x', padx=15, pady=10)

        ttk.Button(control_frame, text="➕ إضافة طالب جديد",
                   command=self.show_add_student_window,
                   style='Success.TButton').pack(side='left', padx=5)

        ttk.Button(control_frame, text="✏ تعديل بيانات طالب",
                   command=self.edit_student,
                   style='Primary.TButton').pack(side='left', padx=5)

        ttk.Button(control_frame, text="🗑 حذف طالب",
                   command=self.delete_student,
                   style='Error.TButton').pack(side='left', padx=5)

        # عرض البيانات الأولية
        self.display_all_students()

    def show_add_student_window(self):
        """عرض نافذة إضافة طالب جديد"""
        add_window = tk.Toplevel(self.root)
        add_window.title("➕ إضافة طالب جديد")
        add_window.geometry("500x600")
        add_window.configure(bg=self.colors['background'])
        add_window.resizable(False, False)

        # جعل النافذة تظهر في المنتصف
        add_window.transient(self.root)
        add_window.grab_set()

        # عنوان النافذة
        title_label = tk.Label(add_window,
                               text="➕ إضافة طالب جديد",
                               bg=self.colors['background'],
                               fg=self.colors['primary'],
                               font=('Arial', 16, 'bold'))
        title_label.pack(pady=15)

        # إطار بيانات الطالب
        form_frame = tk.Frame(add_window, bg=self.colors['background'])
        form_frame.pack(fill='both', expand=True, padx=20, pady=10)

        # الحقول الإلزامية
        fields = [
            ("الرقم القومي (SSN):", "ssn"),
            ("الاسم الأول:", "fname"),
            ("الاسم الأوسط:", "mname"),
            ("الاسم الأخير:", "lname"),
            ("المستوى (1-4):", "level"),
            ("رقم الهاتف:", "phone"),
            ("البريد الإلكتروني:", "email"),
            ("القسم:", "department")
        ]

        self.add_student_entries = {}

        for i, (label, field) in enumerate(fields):
            tk.Label(form_frame, text=label, bg=self.colors['background'],
                     font=('Arial', 10)).grid(row=i, column=0, sticky='w', padx=5, pady=8)

            if field == "level":
                level_var = tk.StringVar()
                level_combo = ttk.Combobox(form_frame, textvariable=level_var,
                                           values=['1', '2', '3', '4'], state='readonly')
                level_combo.grid(row=i, column=1, sticky='ew', padx=5, pady=8)
                self.add_student_entries[field] = level_combo
            elif field == "department":
                # جلب الأقسام من قاعدة البيانات
                dept_combo = ttk.Combobox(form_frame, state='readonly')
                dept_combo.grid(row=i, column=1, sticky='ew', padx=5, pady=8)
                self.add_student_entries[field] = dept_combo
                self.load_departments_to_combo(dept_combo)
            else:
                entry = ttk.Entry(form_frame, font=('Arial', 10))
                entry.grid(row=i, column=1, sticky='ew', padx=5, pady=8)
                self.add_student_entries[field] = entry

        # تعليمات الحقول
        instructions = tk.Label(form_frame,
                                text="ملاحظة: جميع الحقول مطلوبة\nتأكد من صحة البيانات قبل الحفظ",
                                bg=self.colors['background'],
                                fg=self.colors['warning'],
                                font=('Arial', 9))
        instructions.grid(row=len(fields), column=0, columnspan=2, pady=15)

        # أزرار التحكم
        button_frame = tk.Frame(add_window, bg=self.colors['background'])
        button_frame.pack(fill='x', pady=15)

        ttk.Button(button_frame, text="💾 حفظ الطالب",
                   command=self.add_student_to_database,
                   style='Success.TButton').pack(side='left', padx=10)

        ttk.Button(button_frame, text="❌ إلغاء",
                   command=add_window.destroy,
                   style='Error.TButton').pack(side='right', padx=10)

    def load_departments_to_combo(self, combo):
        """تحميل الأقسام في Combobox"""
        if self.db_connection:
            try:
                cursor = self.db_connection.cursor()
                cursor.execute("SELECT DID, DName FROM department ORDER BY DName")
                departments = cursor.fetchall()

                # حفظ بيانات الأقسام للاستخدام لاحقاً
                self.departments_dict = {dept[1]: dept[0] for dept in departments}

                # تعيين القيم في Combobox
                combo['values'] = list(self.departments_dict.keys())

            except Error as e:
                messagebox.showerror("❌ خطأ", f"فشل في تحميل الأقسام: {e}")

    def add_student_to_database(self):
        """إضافة طالب جديد إلى قاعدة البيانات"""
        try:
            # جمع البيانات من الحقول
            data = {}
            for field, widget in self.add_student_entries.items():
                if isinstance(widget, ttk.Combobox):
                    value = widget.get()
                else:
                    value = widget.get()

                if not value:
                    messagebox.showerror("❌ خطأ", f"يرجى ملء جميع الحقول")
                    return

                data[field] = value

            # التحقق من صحة البيانات
            if not self.validate_student_data(data):
                return

            # الحصول على ID القسم
            dept_name = data['department']
            dept_id = self.departments_dict.get(dept_name)

            if not dept_id:
                messagebox.showerror("❌ خطأ", "القسم المحدد غير صحيح")
                return

            if self.db_connection:
                cursor = self.db_connection.cursor()

                # إدخال البيانات في قاعدة البيانات
                query = """
                INSERT INTO student (SSN, FName, MName, LName, level, phone, Email, DID)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """

                values = (
                    data['ssn'],
                    data['fname'],
                    data['mname'],
                    data['lname'],
                    int(data['level']),
                    data['phone'],
                    data['email'],
                    dept_id
                )

                cursor.execute(query, values)
                self.db_connection.commit()

                messagebox.showinfo("✅ نجاح", "تم إضافة الطالب بنجاح!")

                # تحديث الجدول وإغلاق النافذة
                self.display_all_students()

                # البحث عن النافذة الأم وإغلاقها
                for window in self.root.winfo_children():
                    if isinstance(window, tk.Toplevel) and "إضافة طالب جديد" in window.title():
                        window.destroy()
                        break

        except Error as e:
            messagebox.showerror("❌ خطأ", f"فشل في إضافة الطالب: {e}")

    def validate_student_data(self, data):
        """التحقق من صحة بيانات الطالب"""
        try:
            # التحقق من رقم الهاتف
            phone = data['phone']
            if not phone.startswith('01') or len(phone) != 11 or not phone.isdigit():
                messagebox.showerror("❌ خطأ", "رقم الهاتف يجب أن يبدأ بـ 01 ويتكون من 11 رقم")
                return False

            # التحقق من المستوى
            level = int(data['level'])
            if level < 1 or level > 4:
                messagebox.showerror("❌ خطأ", "المستوى يجب أن يكون بين 1 و 4")
                return False

            # التحقق من البريد الإلكتروني (تحقق بسيط)
            email = data['email']
            if '@' not in email or '.' not in email:
                messagebox.showerror("❌ خطأ", "البريد الإلكتروني غير صحيح")
                return False

            # التحقق من الرقم القومي
            ssn = data['ssn']
            if len(ssn) != 14:
                messagebox.showerror("❌ خطأ", "الرقم القومي يجب أن يتكون من 14 رقم")
                return False

            return True

        except ValueError:
            messagebox.showerror("❌ خطأ", "يرجى إدخال بيانات صحيحة")
            return False

    def create_course_tab(self):
        """إنشاء تبويب إدارة المقررات"""
        # إطار البحث
        search_frame = tk.LabelFrame(self.course_tab, text="🔍 بحث المقررات",
                                     bg=self.colors['background'],
                                     fg=self.colors['text_dark'],
                                     font=('Arial', 12, 'bold'),
                                     padx=10, pady=10)
        search_frame.pack(fill='x', padx=15, pady=10)

        tk.Label(search_frame, text="بحث باسم المقرر:",
                 bg=self.colors['background'],
                 font=('Arial', 10)).grid(row=0, column=0, padx=5, pady=5)

        self.course_search_entry = ttk.Entry(search_frame, width=30, font=('Arial', 10))
        self.course_search_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Button(search_frame, text="🔍 بحث",
                   command=self.search_courses,
                   style='Primary.TButton').grid(row=0, column=2, padx=5, pady=5)

        ttk.Button(search_frame, text="🔄 عرض الكل",
                   command=self.display_all_courses,
                   style='Success.TButton').grid(row=0, column=3, padx=5, pady=5)

        # جدول المقررات
        table_frame = tk.Frame(self.course_tab, bg=self.colors['background'])
        table_frame.pack(fill='both', expand=True, padx=15, pady=10)

        columns = ('CID', 'CName', 'C_Hours', 'Department', 'Instructor')
        self.course_tree = ttk.Treeview(table_frame, columns=columns, show='headings', height=15,
                                        style='Custom.Treeview')

        for col in columns:
            self.course_tree.heading(col, text=col)
            self.course_tree.column(col, width=120)

        scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=self.course_tree.yview)
        self.course_tree.configure(yscrollcommand=scrollbar.set)

        self.course_tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        self.display_all_courses()

    def create_enrollment_tab(self):
        """إنشاء تبويب التسجيل في المقررات"""
        main_frame = tk.Frame(self.enrollment_tab, bg=self.colors['background'])
        main_frame.pack(fill='both', expand=True, padx=15, pady=15)

        # قسم اختيار الطالب
        student_frame = tk.LabelFrame(main_frame, text="👤 اختيار الطالب",
                                      bg=self.colors['background'],
                                      fg=self.colors['text_dark'],
                                      font=('Arial', 12, 'bold'),
                                      padx=10, pady=10)
        student_frame.pack(fill='x', pady=10)

        tk.Label(student_frame, text="رقم الطالب:",
                 bg=self.colors['background'],
                 font=('Arial', 10)).grid(row=0, column=0, padx=5, pady=5)

        self.enroll_student_id = ttk.Entry(student_frame, width=20, font=('Arial', 10))
        self.enroll_student_id.grid(row=0, column=1, padx=5, pady=5)

        ttk.Button(student_frame, text="🔍 تحميل المقررات",
                   command=self.load_student_courses,
                   style='Primary.TButton').grid(row=0, column=2, padx=5, pady=5)

        # معلومات الطالب
        self.student_info_label = tk.Label(student_frame,
                                           text="⬅ يرجى إدخال رقم الطالب ثم النقر على 'تحميل المقررات'",
                                           bg=self.colors['background'],
                                           fg=self.colors['primary'],
                                           font=('Arial', 11, 'bold'))
        self.student_info_label.grid(row=1, column=0, columnspan=3, padx=5, pady=10)

        # قسم المقررات المتاحة
        courses_frame = tk.LabelFrame(main_frame, text="📚 المقررات المتاحة",
                                      bg=self.colors['background'],
                                      fg=self.colors['text_dark'],
                                      font=('Arial', 12, 'bold'),
                                      padx=10, pady=10)
        courses_frame.pack(fill='both', expand=True, pady=10)

        # المقررات المسجلة
        registered_frame = tk.Frame(courses_frame, bg=self.colors['background'])
        registered_frame.pack(side='left', fill='both', expand=True, padx=5)

        tk.Label(registered_frame, text="✅ المقررات المسجلة:",
                 bg=self.colors['background'],
                 fg=self.colors['success'],
                 font=('Arial', 11, 'bold')).pack()

        self.registered_listbox = tk.Listbox(registered_frame,
                                             height=12,
                                             font=('Arial', 10),
                                             bg='#d5f4e6',
                                             selectbackground=self.colors['success'])
        self.registered_listbox.pack(fill='both', expand=True, pady=5)

        # المقررات المتاحة للتسجيل
        available_frame = tk.Frame(courses_frame, bg=self.colors['background'])
        available_frame.pack(side='right', fill='both', expand=True, padx=5)

        tk.Label(available_frame, text="📖 المقررات المتاحة:",
                 bg=self.colors['background'],
                 fg=self.colors['primary'],
                 font=('Arial', 11, 'bold')).pack()

        self.available_listbox = tk.Listbox(available_frame,
                                            height=12,
                                            font=('Arial', 10),
                                            bg='#d6eaf8',
                                            selectbackground=self.colors['primary'])
        self.available_listbox.pack(fill='both', expand=True, pady=5)

        # أزرار التحكم
        button_frame = tk.Frame(main_frame, bg=self.colors['background'])
        button_frame.pack(fill='x', pady=15)

        ttk.Button(button_frame, text="🎯 تسجيل في المقرر",
                   command=self.enroll_course,
                   style='Success.TButton').pack(side='left', padx=10)

        ttk.Button(button_frame, text="❌ إلغاء التسجيل",
                   command=self.unenroll_course,
                   style='Error.TButton').pack(side='left', padx=10)

        ttk.Button(button_frame, text="🔄 تحديث القوائم",
                   command=lambda: self.load_student_courses() if self.enroll_student_id.get() else None,
                   style='Primary.TButton').pack(side='right', padx=10)

    def create_reports_tab(self):
        """إنشاء تبويب التقارير"""
        main_frame = tk.Frame(self.reports_tab, bg=self.colors['background'])
        main_frame.pack(fill='both', expand=True, padx=15, pady=15)

        # أزرار التقارير
        reports_frame = tk.LabelFrame(main_frame, text="📈 التقارير المتاحة",
                                      bg=self.colors['background'],
                                      fg=self.colors['text_dark'],
                                      font=('Arial', 12, 'bold'),
                                      padx=10, pady=10)
        reports_frame.pack(fill='x', pady=10)

        # صف أول من الأزرار
        button_row1 = tk.Frame(reports_frame, bg=self.colors['background'])
        button_row1.pack(fill='x', pady=5)

        ttk.Button(button_row1, text="👥 عرض جميع الطلاب",
                   command=self.report_all_students,
                   style='Primary.TButton').pack(side='left', padx=5, pady=2, fill='x', expand=True)

        ttk.Button(button_row1, text="📚 عرض جميع المقررات",
                   command=self.report_all_courses,
                   style='Primary.TButton').pack(side='left', padx=5, pady=2, fill='x', expand=True)

        # صف ثاني من الأزرار
        button_row2 = tk.Frame(reports_frame, bg=self.colors['background'])
        button_row2.pack(fill='x', pady=5)

        ttk.Button(button_row2, text="🏫 الطلاب حسب القسم",
                   command=self.report_students_by_department,
                   style='Success.TButton').pack(side='left', padx=5, pady=2, fill='x', expand=True)

        ttk.Button(button_row2, text="📊 المقررات حسب القسم",
                   command=self.report_courses_by_department,
                   style='Success.TButton').pack(side='left', padx=5, pady=2, fill='x', expand=True)

        # منطقة عرض التقرير
        text_frame = tk.Frame(main_frame, bg=self.colors['background'])
        text_frame.pack(fill='both', expand=True, pady=10)

        self.report_text = tk.Text(text_frame,
                                   height=20,
                                   width=100,
                                   font=('Arial', 10),
                                   bg='#f8f9fa',
                                   fg=self.colors['text_dark'],
                                   wrap='word')

        scrollbar = tk.Scrollbar(text_frame, command=self.report_text.yview)
        self.report_text.configure(yscrollcommand=scrollbar.set)

        self.report_text.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        # أزرار التحكم بالتقرير
        control_frame = tk.Frame(main_frame, bg=self.colors['background'])
        control_frame.pack(fill='x', pady=10)

        ttk.Button(control_frame, text="🗑 مسح التقرير",
                   command=self.clear_report,
                   style='Warning.TButton').pack(side='left', padx=5)

        ttk.Button(control_frame, text="💾 تصدير التقرير",
                   command=self.export_report,
                   style='Success.TButton').pack(side='left', padx=5)

        ttk.Button(control_frame, text="🖨 طباعة التقرير",
                   command=self.print_report,
                   style='Primary.TButton').pack(side='left', padx=5)

    # دوال التعامل مع قاعدة البيانات (نفس الدوال السابقة)
    def display_all_students(self):
        """عرض جميع الطلاب"""
        if self.db_connection:
            try:
                cursor = self.db_connection.cursor()
                query = """
                SELECT s.SID, s.SSN, s.FName, s.MName, s.LName, s.level, d.DName, s.phone, s.Email
                FROM student s
                LEFT JOIN department d ON s.DID = d.DID
                """
                cursor.execute(query)
                rows = cursor.fetchall()

                # مسح البيانات القديمة
                for item in self.student_tree.get_children():
                    self.student_tree.delete(item)

                # إضافة البيانات الجديدة
                for row in rows:
                    self.student_tree.insert('', 'end', values=row)

                # تحديث الإحصائيات
                self.update_student_stats(len(rows))

            except Error as e:
                messagebox.showerror("❌ خطأ", f"فشل في جلب بيانات الطلاب: {e}")

    def display_all_courses(self):
        """عرض جميع المقررات"""
        if self.db_connection:
            try:
                cursor = self.db_connection.cursor()
                query = """
                SELECT c.CID, c.CName, c.C_Hours, d.DName, CONCAT(i.FName, ' ', i.LName)
                FROM course c
                LEFT JOIN course_department cd ON c.CID = cd.CID
                LEFT JOIN department d ON cd.DID = d.DID
                LEFT JOIN instructor_course ic ON c.CID = ic.CID
                LEFT JOIN instructor i ON ic.IID = i.IID
                """
                cursor.execute(query)
                rows = cursor.fetchall()

                for item in self.course_tree.get_children():
                    self.course_tree.delete(item)

                for row in rows:
                    self.course_tree.insert('', 'end', values=row)

            except Error as e:
                messagebox.showerror("❌ خطأ", f"فشل في جلب بيانات المقررات: {e}")

    def search_students(self):
        """بحث الطلاب"""
        search_term = self.student_search_entry.get()
        if not search_term:
            self.display_all_students()
            return

        if self.db_connection:
            try:
                cursor = self.db_connection.cursor()
                query = """
                SELECT s.SID, s.SSN, s.FName, s.MName, s.LName, s.level, d.DName, s.phone, s.Email
                FROM student s
                LEFT JOIN department d ON s.DID = d.DID
                WHERE s.FName LIKE %s OR s.LName LIKE %s OR s.SSN LIKE %s
                """
                cursor.execute(query, (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))
                rows = cursor.fetchall()

                for item in self.student_tree.get_children():
                    self.student_tree.delete(item)

                for row in rows:
                    self.student_tree.insert('', 'end', values=row)

                messagebox.showinfo("✅ نجاح", f"تم العثور على {len(rows)} طالب")

            except Error as e:
                messagebox.showerror("❌ خطأ", f"فشل في البحث: {e}")

    def search_courses(self):
        """بحث المقررات"""
        search_term = self.course_search_entry.get()
        if not search_term:
            self.display_all_courses()
            return

        if self.db_connection:
            try:
                cursor = self.db_connection.cursor()
                query = """
                SELECT c.CID, c.CName, c.C_Hours, d.DName, CONCAT(i.FName, ' ', i.LName)
                FROM course c
                LEFT JOIN course_department cd ON c.CID = cd.CID
                LEFT JOIN department d ON cd.DID = d.DID
                LEFT JOIN instructor_course ic ON c.CID = ic.CID
                LEFT JOIN instructor i ON ic.IID = i.IID
                WHERE c.CName LIKE %s
                """
                cursor.execute(query, (f'%{search_term}%',))
                rows = cursor.fetchall()

                for item in self.course_tree.get_children():
                    self.course_tree.delete(item)

                for row in rows:
                    self.course_tree.insert('', 'end', values=row)

                messagebox.showinfo("✅ نجاح", f"تم العثور على {len(rows)} مقرر")

            except Error as e:
                messagebox.showerror("❌ خطأ", f"فشل في البحث: {e}")

    def load_student_courses(self):
        """تحميل مقررات الطالب"""
        student_id = self.enroll_student_id.get()
        if not student_id:
            messagebox.showwarning("⚠ تنبيه", "يرجى إدخال رقم الطالب")
            return

        if self.db_connection:
            try:
                cursor = self.db_connection.cursor()

                # معلومات الطالب
                cursor.execute("SELECT FName, MName, LName, level FROM student WHERE SID = %s", (student_id,))
                student = cursor.fetchone()

                if student:
                    self.student_info_label.config(
                        text=f"👤 الطالب: {student[0]} {student[1]} {student[2]} | المستوى: {student[3]}",
                        fg=self.colors['success']
                    )
                else:
                    messagebox.showerror("❌ خطأ", "لم يتم العثور على الطالب")
                    return

                # المقررات المسجلة
                self.registered_listbox.delete(0, tk.END)
                query = """
                SELECT c.CID, c.CName 
                FROM enrollment e 
                JOIN course c ON e.CID = c.CID 
                WHERE e.SID = %s
                """
                cursor.execute(query, (student_id,))
                registered_courses = cursor.fetchall()

                for course in registered_courses:
                    self.registered_listbox.insert(tk.END, f"{course[0]} - {course[1]}")

                # المقررات المتاحة
                self.available_listbox.delete(0, tk.END)
                query = """
                SELECT c.CID, c.CName 
                FROM course c 
                WHERE c.CID NOT IN (
                    SELECT CID FROM enrollment WHERE SID = %s
                )
                """
                cursor.execute(query, (student_id,))
                available_courses = cursor.fetchall()

                for course in available_courses:
                    self.available_listbox.insert(tk.END, f"{course[0]} - {course[1]}")

                messagebox.showinfo("✅ نجاح",
                                    f"تم تحميل {len(registered_courses)} مقرر مسجل و {len(available_courses)} مقرر متاح")

            except Error as e:
                messagebox.showerror("❌ خطأ", f"فشل في تحميل المقررات: {e}")

    def enroll_course(self):
        """تسجيل الطالب في مقرر"""
        student_id = self.enroll_student_id.get()
        selected = self.available_listbox.curselection()

        if not student_id or not selected:
            messagebox.showwarning("⚠ تنبيه", "يرجى اختيار الطالب والمقرر")
            return

        course_text = self.available_listbox.get(selected[0])
        course_id = course_text.split(' - ')[0]

        if self.db_connection:
            try:
                cursor = self.db_connection.cursor()
                cursor.execute("INSERT INTO enrollment (SID, CID) VALUES (%s, %s)", (student_id, course_id))
                self.db_connection.commit()
                messagebox.showinfo("✅ نجاح", "تم تسجيل المقرر بنجاح!")
                self.load_student_courses()  # تحديث القوائم
            except Error as e:
                messagebox.showerror("❌ خطأ", f"فشل في التسجيل: {e}")

    def unenroll_course(self):
        """إلغاء تسجيل الطالب من مقرر"""
        student_id = self.enroll_student_id.get()
        selected = self.registered_listbox.curselection()

        if not student_id or not selected:
            messagebox.showwarning("⚠ تنبيه", "يرجى اختيار الطالب والمقرر")
            return

        course_text = self.registered_listbox.get(selected[0])
        course_id = course_text.split(' - ')[0]

        if self.db_connection:
            try:
                cursor = self.db_connection.cursor()
                cursor.execute("DELETE FROM enrollment WHERE SID = %s AND CID = %s", (student_id, course_id))
                self.db_connection.commit()
                messagebox.showinfo("✅ نجاح", "تم إلغاء التسجيل بنجاح!")
                self.load_student_courses()  # تحديث القوائم
            except Error as e:
                messagebox.showerror("❌ خطأ", f"فشل في إلغاء التسجيل: {e}")

    # دوال التقارير (نفس الدوال السابقة مع تحسينات بصرية)
    def report_all_students(self):
        """تقرير جميع الطلاب"""
        if self.db_connection:
            try:
                cursor = self.db_connection.cursor()
                query = """
                SELECT s.SID, s.FName, s.MName, s.LName, s.level, d.DName, s.Email
                FROM student s
                LEFT JOIN department d ON s.DID = d.DID
                ORDER BY d.DName, s.level
                """
                cursor.execute(query)
                rows = cursor.fetchall()

                self.report_text.delete(1.0, tk.END)
                self.report_text.insert(tk.END, "📊 تقرير جميع الطلاب\n", "header")
                self.report_text.insert(tk.END, "=" * 60 + "\n\n")

                for i, row in enumerate(rows, 1):
                    self.report_text.insert(tk.END, f"🎓 الطالب #{i}\n", "subheader")
                    self.report_text.insert(tk.END, f"   رقم الطالب: {row[0]}\n")
                    self.report_text.insert(tk.END, f"   الاسم: {row[1]} {row[2]} {row[3]}\n")
                    self.report_text.insert(tk.END, f"   المستوى: {row[4]}\n")
                    self.report_text.insert(tk.END, f"   القسم: {row[5]}\n")
                    self.report_text.insert(tk.END, f"   البريد الإلكتروني: {row[6]}\n")
                    self.report_text.insert(tk.END, "-" * 40 + "\n")

                self.report_text.insert(tk.END, f"\n📈 إجمالي عدد الطلاب: {len(rows)} طالب\n", "footer")

            except Error as e:
                messagebox.showerror("❌ خطأ", f"فشل في إنشاء التقرير: {e}")

    def report_all_courses(self):
        """تقرير جميع المقررات"""
        if self.db_connection:
            try:
                cursor = self.db_connection.cursor()
                query = """
                SELECT c.CID, c.CName, c.C_Hours, d.DName, CONCAT(i.FName, ' ', i.LName)
                FROM course c
                LEFT JOIN course_department cd ON c.CID = cd.CID
                LEFT JOIN department d ON cd.DID = d.DID
                LEFT JOIN instructor_course ic ON c.CID = ic.CID
                LEFT JOIN instructor i ON ic.IID = i.IID
                ORDER BY d.DName
                """
                cursor.execute(query)
                rows = cursor.fetchall()

                self.report_text.delete(1.0, tk.END)
                self.report_text.insert(tk.END, "📚 تقرير جميع المقررات\n", "header")
                self.report_text.insert(tk.END, "=" * 60 + "\n\n")

                for i, row in enumerate(rows, 1):
                    self.report_text.insert(tk.END, f"📖 المقرر #{i}\n", "subheader")
                    self.report_text.insert(tk.END, f"   رقم المقرر: {row[0]}\n")
                    self.report_text.insert(tk.END, f"   اسم المقرر: {row[1]}\n")
                    self.report_text.insert(tk.END, f"   الساعات: {row[2]}\n")
                    self.report_text.insert(tk.END, f"   القسم: {row[3]}\n")
                    self.report_text.insert(tk.END, f"   المحاضر: {row[4]}\n")
                    self.report_text.insert(tk.END, "-" * 40 + "\n")

                self.report_text.insert(tk.END, f"\n📈 إجمالي عدد المقررات: {len(rows)} مقرر\n", "footer")

            except Error as e:
                messagebox.showerror("❌ خطأ", f"فشل في إنشاء التقرير: {e}")

    def report_students_by_department(self):
        """تقرير الطلاب حسب الأقسام"""
        if self.db_connection:
            try:
                cursor = self.db_connection.cursor()
                query = """
                SELECT d.DName, COUNT(s.SID) as StudentCount
                FROM department d
                LEFT JOIN student s ON d.DID = s.DID
                GROUP BY d.DID, d.DName
                ORDER BY StudentCount DESC
                """
                cursor.execute(query)
                rows = cursor.fetchall()

                self.report_text.delete(1.0, tk.END)
                self.report_text.insert(tk.END, "🏫 تقرير الطلاب حسب الأقسام\n", "header")
                self.report_text.insert(tk.END, "=" * 60 + "\n\n")

                total_students = 0
                for row in rows:
                    self.report_text.insert(tk.END, f"📊 {row[0]}\n", "subheader")
                    self.report_text.insert(tk.END, f"   عدد الطلاب: {row[1]}\n")
                    self.report_text.insert(tk.END, "-" * 30 + "\n")
                    total_students += row[1]

                self.report_text.insert(tk.END, f"\n📈 الإجمالي العام: {total_students} طالب\n", "footer")

            except Error as e:
                messagebox.showerror("❌ خطأ", f"فشل في إنشاء التقرير: {e}")

    def report_courses_by_department(self):
        """تقرير المقررات حسب الأقسام"""
        if self.db_connection:
            try:
                cursor = self.db_connection.cursor()
                query = """
                SELECT d.DName, COUNT(c.CID) as CourseCount
                FROM department d
                LEFT JOIN course_department cd ON d.DID = cd.DID
                LEFT JOIN course c ON cd.CID = c.CID
                GROUP BY d.DID, d.DName
                ORDER BY CourseCount DESC
                """
                cursor.execute(query)
                rows = cursor.fetchall()

                self.report_text.delete(1.0, tk.END)
                self.report_text.insert(tk.END, "📊 تقرير المقررات حسب الأقسام\n", "header")
                self.report_text.insert(tk.END, "=" * 60 + "\n\n")

                total_courses = 0
                for row in rows:
                    self.report_text.insert(tk.END, f"📚 {row[0]}\n", "subheader")
                    self.report_text.insert(tk.END, f"   عدد المقررات: {row[1]}\n")
                    self.report_text.insert(tk.END, "-" * 30 + "\n")
                    total_courses += row[1]

                self.report_text.insert(tk.END, f"\n📈 الإجمالي العام: {total_courses} مقرر\n", "footer")

            except Error as e:
                messagebox.showerror("❌ خطأ", f"فشل في إنشاء التقرير: {e}")

    def clear_report(self):
        """مسح التقرير"""
        self.report_text.delete(1.0, tk.END)
        messagebox.showinfo("✅ نجاح", "تم مسح التقرير")

    def export_report(self):
        """تصدير التقرير"""
        content = self.report_text.get(1.0, tk.END)
        if content.strip():
            try:
                with open("university_report.txt", "w", encoding="utf-8") as f:
                    f.write(content)
                messagebox.showinfo("✅ نجاح", "تم تصدير التقرير بنجاح إلى university_report.txt")
            except Exception as e:
                messagebox.showerror("❌ خطأ", f"فشل في تصدير التقرير: {e}")
        else:
            messagebox.showwarning("⚠ تنبيه", "لا يوجد محتوى لتصديره")

    def print_report(self):
        """طباعة التقرير"""
        content = self.report_text.get(1.0, tk.END)
        if content.strip():
            messagebox.showinfo("🖨 طباعة", "تم إرسال التقرير للطباعة (وظيفة تجريبية)")
        else:
            messagebox.showwarning("⚠ تنبيه", "لا يوجد محتوى للطباعة")

    def update_student_stats(self, count):
        """تحديث إحصائيات الطلاب"""
        # يمكن استخدام هذه الدالة لتحديث الإحصائيات في المستقبل
        pass

    def add_student(self):
        """إضافة طالب جديد - دالة قديمة"""
        self.show_add_student_window()

    def edit_student(self):
        """تعديل بيانات طالب"""
        selected = self.student_tree.selection()
        if not selected:
            messagebox.showwarning("⚠ تنبيه", "يرجى اختيار طالب للتعديل")
            return
        messagebox.showinfo("✏ تعديل طالب", "سيتم تنفيذ هذه الميزة قريباً!")

    def delete_student(self):
        """حذف طالب"""
        selected = self.student_tree.selection()
        if not selected:
            messagebox.showwarning("⚠ تنبيه", "يرجى اختيار طالب للحذف")
            return

        student_id = self.student_tree.item(selected[0])['values'][0]
        student_name = f"{self.student_tree.item(selected[0])['values'][2]} {self.student_tree.item(selected[0])['values'][4]}"

        if messagebox.askyesno("⚠ تأكيد الحذف",
                               f"هل أنت متأكد من حذف الطالب:\n{student_name} (رقم: {student_id})؟"):
            if self.db_connection:
                try:
                    cursor = self.db_connection.cursor()
                    cursor.execute("DELETE FROM student WHERE SID = %s", (student_id,))
                    self.db_connection.commit()
                    messagebox.showinfo("✅ نجاح", "تم حذف الطالب بنجاح")
                    self.display_all_students()
                except Error as e:
                    messagebox.showerror("❌ خطأ", f"فشل في حذف الطالب: {e}")


def main():
    root = tk.Tk()
    app = ModernUniversityRegistrationSystem(root)
    root.mainloop()


if __name__ == "__main__":
    main()