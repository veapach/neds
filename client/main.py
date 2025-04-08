import flet as ft
from pages.auth import auth


async def main(page: ft.Page):
    page.title = "NEDS"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#1e1e2f"
    await auth(page)


ft.app(target=main)
