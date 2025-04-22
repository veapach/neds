import flet as ft
import asyncio
from pages.auth import auth


async def main(page: ft.Page):
    page.title = "NEDS"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#1e1e2f"
    page.window.maximized = True

    def on_resized(e):
        page.update()

    page.on_resized = on_resized

    await auth(page)


ft.app(target=main)
