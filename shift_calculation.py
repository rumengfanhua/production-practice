# -*- coding: utf-8 -*-
"""
Программа для расчета выполнения сменного задания на нефтеперерабатывающем заводе
АО «Куйбышевский нефтеперерабатывающий завод»
"""

import os
from datetime import datetime

def calculate_shift_task():
    print("=" * 60)
    print("  Программа расчета выполнения сменного задания АО «КНПЗ»")
    print("=" * 60)

    # 1. Запрос данных у пользователя
    try:
        product_name = input("\nВведите название продукта: ").strip()
        plan_tons = float(input("Введите плановое задание на смену (в тоннах): "))
        fact_tons = float(input("Введите фактически произведенное количество (в тоннах): "))
    except ValueError:
        print("\n❌ Ошибка: Пожалуйста, введите числовые значения для плана и факта!")
        return

    # 2. Расчет процента выполнения плана
    if plan_tons <= 0:
        print("\n❌ Ошибка: Плановое задание должно быть больше нуля!")
        return
    
    completion_percent = (fact_tons / plan_tons) * 100

    # 3. Определение результата
    if completion_percent >= 100:
        result_status = "План выполнен ✅"
    else:
        result_status = "План не выполнен ❌"

    # 4. Вывод результатов на экран
    print("\n" + "-" * 60)
    print("📊 РЕЗУЛЬТАТЫ СМЕННОГО ЗАДАНИЯ")
    print(f"Продукт:                {product_name}")
    print(f"Плановое задание:       {plan_tons:.2f} тонн")
    print(f"Фактическая выработка:  {fact_tons:.2f} тонн")
    print(f"Процент выполнения:     {completion_percent:.2f}%")
    print(f"Статус:                 {result_status}")
    print("-" * 60)

    # 5. Запись результатов в файл для отчетности
    log_file = "shift_report_knpz.txt"
    current_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    
    # Формируем строку для записи
    log_entry = (
        f"[{current_time}] | Продукт: {product_name} | План: {plan_tons:.2f} т | "
        f"Факт: {fact_tons:.2f} т | Выполнение: {completion_percent:.2f}% | Статус: {result_status}\n"
    )

    # Записываем в файл (режим добавления 'a')
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(log_entry)
        print(f"\n✅ Результаты успешно сохранены в файл: {log_file}")
    except Exception as e:
        print(f"\n⚠️ Предупреждение: Не удалось записать в файл. Ошибка: {e}")

if __name__ == "__main__":
    calculate_shift_task()