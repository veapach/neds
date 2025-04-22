import flet as ft
import asyncio


async def main_page(page: ft.Page, username: str):
    page.title = "NEDS"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#1e1e2f"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER

    welcome_text = ft.Text(
        "Добро пожаловать,",
        size=30,
        weight="bold",
        color="white",
        text_align=ft.TextAlign.CENTER,
        offset=ft.transform.Offset(0, 0.1),
        opacity=1,
        animate_opacity=ft.Animation(500, ft.AnimationCurve.EASE_OUT),
        animate_size=ft.Animation(500, ft.AnimationCurve.EASE_OUT),
        animate_offset=ft.Animation(500, ft.AnimationCurve.EASE_OUT),
    )

    username_text = ft.Text(
        f"{username}",
        size=48,
        weight="bold",
        color="purple",
        text_align=ft.TextAlign.CENTER,
        opacity=0,
        offset=ft.transform.Offset(0, 0.5),
        animate_opacity=ft.Animation(500, ft.AnimationCurve.EASE_OUT),
        animate_offset=ft.Animation(500, ft.AnimationCurve.EASE_OUT),
    )

    menu = ft.Row(
        [
            ft.ElevatedButton("Голосовой чат"),
            ft.ElevatedButton("Чат"),
            ft.ElevatedButton("Настройки"),
            ft.ElevatedButton("Выход"),
        ],
        opacity=0,
        offset=ft.transform.Offset(0, 0.1),
        alignment=ft.CrossAxisAlignment.CENTER,
        animate_opacity=ft.Animation(500, ft.AnimationCurve.EASE_OUT),
        animate_offset=ft.Animation(500, ft.AnimationCurve.EASE_OUT),
    )

    content = ft.Column(
        [welcome_text, username_text, menu],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        width=page.width,
    )

    await asyncio.sleep(0.5)

    page.add(content)

    await asyncio.sleep(1)

    welcome_text.offset = ft.transform.Offset(0, -0.3)
    welcome_text.size = 26
    page.update()

    await asyncio.sleep(1)

    username_text.opacity = 1
    username_text.offset = ft.transform.Offset(0, 0)
    page.update()

    await asyncio.sleep(2)

    welcome_text.size = 80
    welcome_text.opacity = 0
    welcome_text.offset = ft.transform.Offset(0, -2)

    username_text.opacity = 0
    username_text.offset = ft.transform.Offset(0, -1)
    page.update()

    await asyncio.sleep(1)

    menu.opacity = 1
    menu.offset = ft.transform.Offset(0, 0)
    page.update()
