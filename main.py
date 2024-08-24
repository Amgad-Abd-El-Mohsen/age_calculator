import flet as ft
import datetime

bd_now = datetime.datetime.now()
dp_bd = ' '

def main(page: ft.Page):

    def age(x):
        calc_age = bd_now-dp_bd
        print(calc_age)
        calc_year = calc_age.days / 365
        print('='*50)
        print(bd_now-dp_bd)
        print(calc_year)
        print('='*50)
        t.value = f"hi {a.value}"
        tt.value = (
        f"You lived {calc_year:.2f} years\n"
        f"or {calc_year * 12:.2f} months\n"
        f"or {calc_year * 52.1775:.2f} weeks\n"
        f"or {calc_year * 365.25:.2f} days\n"
        f"or {calc_year * 365.25 * 24:.2f} hours\n"
        f"or {calc_year * 365.25 * 24 * 60:.2f} minutes\n"
        f"or {calc_year * 365.25 * 24 * 60 * 60:.2f} seconds\n"
)
        page.update()

    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
    page.title = "AGE CALCULATE"

    page.appbar = ft.AppBar(
        title=ft.Text("AGE CALCULATE"),
        center_title=True,
        bgcolor=ft.colors.BLUE,
        automatically_imply_leading=False,
    )
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.colors.BLUE,
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.Container(expand=True),
                ft.IconButton(icon=ft.icons.INFO_OUTLINE,
                            icon_color=ft.colors.WHITE, on_click=lambda _: page.open(bs))
            ]
        ),
    )
    a = ft.TextField(
        label="my name",
        hint_text="amgad abd el mohsen",
        prefix_icon=ft.icons.TAG_FACES_SHARP,
        filled=True,
    )
    
    def open_datepicker(*args):
        page.open(dp)

    def handle_change(e):
        global dp_bd
        dp_bd = e.control.value
        # page.add(ft.Text(f"Date changed: {e.control.value.strftime('%Y-%m-%d')}"))

    def handle_dismissal(e):
        page.add(ft.Text(f"DatePicker dismissed"))

    dp = ft.DatePicker(
                first_date=datetime.datetime(year=1900, month=10, day=1),
                last_date=datetime.datetime.now(),
                on_change=handle_change,
                on_dismiss=handle_dismissal,
            )

    b = ft.ElevatedButton(
        "Pick date",
        ft.icons.CALENDAR_MONTH,
        on_click=open_datepicker,
    )

    t = ft.Text(size=20, color='blue')
    tt = ft.Text(size=20, color='blue')

    bs = ft.BottomSheet(
        content=ft.Container(
            padding=50,
            content=ft.Column(
                tight=True,
                controls=[
                    ft.Text(
                        "This is made by \namgad abd el mohsen \n( boogeyman ) "),
                    ft.ElevatedButton(
                        "Close", on_click=lambda _: page.close(bs)),
                ],
            ),
        ),
    )

    page.add(
        ft.SafeArea(
            ft.ResponsiveRow(
                [
                    ft.Column(col=12, controls=[a]),                    
                    ft.Container(
                    content=b,
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.top_center,
                    width=150,
                    border_radius=10,
                ),
                    ft.Column(col=12, controls=[t]),
                    ft.Column(col=12, controls=[tt]),

                ],
            ),
        ),
        ft.FloatingActionButton(icon=ft.icons.CALCULATE, on_click=age),



    )


ft.app(target=main)
