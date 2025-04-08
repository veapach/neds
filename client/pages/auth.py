import flet as ft
import requests
import asyncio
from pages.main_page import main_page


async def auth(page: ft.Page):
    page.title = "Авторизация"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#1e1e2f"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    is_login = True

    title = ft.Text(
        "Вход", size=30, weight="bold", color="white", text_align=ft.TextAlign.CENTER
    )
    username = ft.TextField(
        label="Логин", width=300, border_color="purple", text_align=ft.TextAlign.CENTER
    )
    password = ft.TextField(
        label="Пароль",
        width=300,
        password=True,
        can_reveal_password=True,
        border_color="purple",
        text_align=ft.TextAlign.CENTER,
    )

    result = ft.Text("", color="white", text_align=ft.TextAlign.CENTER)

    switch_button = ft.ElevatedButton(
        text="Перейти к регистрации", bgcolor="darkblue", color="white", width=300
    )
    submit_button = ft.ElevatedButton(
        text="Войти", bgcolor="purple", color="white", width=300
    )

    def switch_mode(e):
        nonlocal is_login
        is_login = not is_login
        if is_login:
            title.value = "Вход"
            submit_button.text = "Войти"
            switch_button.text = "Перейти к регистрации"
        else:
            title.value = "Регистрация"
            submit_button.text = "Зарегистрироваться"
            switch_button.text = "Уже есть аккаунт"
        page.update()

    async def submit(e):
        if is_login:
            await login(username.value, password.value)
        else:
            await register(username.value, password.value)

    def reset_field_colors(e):
        username.border_color = "purple"
        password.border_color = "purple"
        result.value = ""
        page.update()

    username.on_change = reset_field_colors
    password.on_change = reset_field_colors

    async def login(username_value, password_value):
        url = "http://localhost:8080/login"
        json = {"username": username_value, "password": password_value}
        try:
            r = requests.post(url, json=json)
            if r.status_code == 200:
                username.border_color = "green"
                password.border_color = "green"
                result.color = "green"
                result.value = "Успешная авторизация"
                page.update()

                await asyncio.sleep(2)

                page.clean()
                await main_page(page, username_value)

            else:
                username.border_color = "red"
                password.border_color = "red"
                result.color = "red"
                result.value = "Ошибка авторизации"
        except requests.exceptions.RequestException:
            result.value = "Ошибка на стороне сервера"
        page.update()

    async def register(username_value, password_value):
        url = "http://localhost:8080/register"
        json = {"username": username_value, "password": password_value}
        try:
            r = requests.post(url, json=json)
            if r.status_code == 200:
                username.border_color = "green"
                password.border_color = "green"
                result.color = "green"
                result.value = "Успешная регистрация"
            else:
                username.border_color = "red"
                password.border_color = "red"
                result.color = "red"
                result.value = "Ошибка регистрации"
        except requests.exceptions.RequestException:
            result.value = "Ошибка на стороне сервера"
        page.update()

    switch_button.on_click = switch_mode
    submit_button.on_click = submit

    page.add(
        ft.Column(
            [
                title,
                username,
                password,
                submit_button,
                switch_button,
                result,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            width=page.width,
        )
    )
