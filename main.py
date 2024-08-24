import flet as ft
import datetime

bd_now = datetime.datetime.now()



def main(page: ft.Page):
    



    def age (x) :
        t.value= f"hi {a.value}"
        tt.value= f"you lived {b.value} year\nor {int(b.value)*12} mounth\nor {int(b.value)*12*4} week\nor {int(b.value)*365} day\nor {int(b.value)*365*24} hour\nor {int(b.value)*365*24*60} min\nor {int(b.value)*365*24*60*60} sec\n"
        page.update()



    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
    page.title="AGE CALCULATE"

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
                ft.IconButton(icon=ft.icons.MENU, icon_color=ft.colors.WHITE),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.icons.FAVORITE, icon_color=ft.colors.WHITE,on_click=lambda _: page.open(bs))
            ]
        ),
    )
    a=   ft.TextField(
            label="my name",
            hint_text="amgad abd el mohsen",
            prefix_icon=ft.icons.TAG_FACES_SHARP,
            filled=True,
        )
    b=   ft.TextField(
            label="My  age",
            hint_text="19",
            prefix_icon=ft.icons.TODAY,
            filled=True,
        )
    t = ft.Text(size=20,color='blue')
    tt = ft.Text(size=20,color='blue')
    

    bs = ft.BottomSheet(
        content=ft.Container(
            padding=50,
            content=ft.Column(
                tight=True,
                controls=[
                    ft.Text("This is made by \namgad abd el mohsen \n( boogeyman ) "),
                    ft.ElevatedButton("Close", on_click=lambda _: page.close(bs)),
                ],
            ),
        ),
    )

    page.add(
        ft.SafeArea(
            ft.ResponsiveRow(
                [
                    ft.Column(col=6, controls=[a]),
                    ft.Column(col=6, controls=[b]),
                    ft.Column(col=12, controls=[t]),
                    ft.Column(col=6, controls=[tt]),
                    
                ],
            ),
        ),
        ft.FloatingActionButton(icon=ft.icons.CALCULATE,on_click=age,)
        
        
        )


ft.app(target=main)
