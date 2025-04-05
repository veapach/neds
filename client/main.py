import flet as ft


def main(page: ft.Page):
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

    switch_button.on_click = switch_mode

    page.add(
        ft.Column(
            [
                title,
                username,
                password,
                submit_button,
                switch_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            width=page.width,
        )
    )


ft.app(target=main)
