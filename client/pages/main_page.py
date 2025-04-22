import flet as ft
import asyncio


async def main_page(page: ft.Page, username: str):
    page.title = "NEDS"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#1e1e2f"
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 0
    page.spacing = 0
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.expand = True

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

    nav_bar = ft.Container(
        content=ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.icons.HEADSET_MIC, icon_size=30, tooltip="Голосовой чат"
                ),
                ft.IconButton(icon=ft.icons.CHAT_BUBBLE, icon_size=30, tooltip="Чат"),
                ft.IconButton(
                    icon=ft.icons.SETTINGS, icon_size=30, tooltip="Настройки"
                ),
                ft.IconButton(icon=ft.icons.LOGOUT, icon_size=30, tooltip="Выход"),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        ),
        height=page.height * 0.12,
        bgcolor="#494980",
        border_radius=ft.border_radius.all(25),
        padding=15,
        margin=ft.margin.only(bottom=30, left=30, right=30, top=40),
    )

    menu = ft.Column(
        [nav_bar],
        opacity=0,
        offset=ft.transform.Offset(0, 0.1),
        alignment=ft.MainAxisAlignment.END,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        animate_opacity=ft.Animation(500, ft.AnimationCurve.EASE_OUT),
        animate_offset=ft.Animation(500, ft.AnimationCurve.EASE_OUT),
        expand=True,
    )

    content = ft.Column(
        [welcome_text, username_text, menu],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        width=page.width,
        expand=True,
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
