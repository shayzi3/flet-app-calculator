import flet as ft 


class Main:
     def __init__(self, page: ft.Page) -> None:
          self.page = page
          
          self.page.title = 'Calculator'
          self.page.window_width = 300
          self.page.window_height = 325
          
          my = MyApp(page)
          my.logic()
          
          
          
class MyApp:
     def __init__(self, page: ft.Page) -> None:
          self.page = page
          self.values: str = ''
          self.newly: list = []
          
     
     def logic(self):
          def clicked(e: ft.ControlEvent) -> None:
               bad = ['+', '-', '*', '/', '%', 'C', '.']
               
               if self.values == '0' and e.control.data not in bad:
                    self.values = e.control.data
                    
                    texter.value = self.values
                    return self.page.update()
               
               if not self.values:
                    if e.control.data not in bad:
                         self.values += e.control.data
                         
                         texter.value = self.values
                         return self.page.update()
                         
               if e.control.data == 'C':
                    self.values = ''
                    
                    texter.value = self.values
                    return self.page.update()
               
               
               if e.control.data != self.values[-1] or e.control.data not in bad:
                    if self.values[-1] not in bad or e.control.data not in bad:
                         
                         self.values += e.control.data
                         
                         texter.value = self.values
                         return self.page.update()
                         
          def equals(e: ft.ControlEvent) -> None:
               self.values = ''
               
               try:
                    self.values = str(eval(texter.value))
                    
                    texter.value = self.values
                    self.page.update()
               
               except (ZeroDivisionError, ValueError, SyntaxError) as ex_:
                    texter.value = self.values
                    self.page.update()
                    
          def clear_one(e: ft.ControlEvent) -> None:     
               self.values = self.values[:-1]
                         
               texter.value = self.values
               self.page.update()
                      
          texter = ft.CupertinoTextField(
               disabled=True,
               height=55,
               text_align=ft.TextAlign.END
          )
          
          first_row = ft.Row(
               controls=[
                    ft.ElevatedButton(text='C', color='red', on_click=clicked, data='C'),
                    ft.ElevatedButton(text='x', color='white', on_click=clear_one, data='x', width=50, bgcolor='orange'),
                    ft.ElevatedButton(text='%', color='white', on_click=clicked, data='%'),
                    ft.ElevatedButton(text='/', color='white', on_click=clicked, data='/')
                    
               ]
          )
          
          second_row = ft.Row(
               controls=[
                    ft.ElevatedButton(text='7', color='white', on_click=clicked, data='7'),
                    ft.ElevatedButton(text='8', color='white', on_click=clicked, data='8'),
                    ft.ElevatedButton(text='9', color='white', on_click=clicked, data='9', bgcolor='orange'),
                    ft.ElevatedButton(text='*', color='white', on_click=clicked, data='*')
               ]
          )
          
          third_row = ft.Row(
               controls=[
                    ft.ElevatedButton(text='4', color='white', on_click=clicked, data='4'),
                    ft.ElevatedButton(text='5', color='white', on_click=clicked, data='5'),
                    ft.ElevatedButton(text='6', color='white', on_click=clicked, data='6'),
                    ft.ElevatedButton(text='-', color='white', on_click=clicked, data='-', bgcolor='orange')
               ]
          )
          
          fourth_row = ft.Row(
               controls=[
                    ft.ElevatedButton(text='1', color='white', on_click=clicked, data='1'),
                    ft.ElevatedButton(text='2', color='white', on_click=clicked, data='2'),
                    ft.ElevatedButton(text='3', color='white', on_click=clicked, data='3', bgcolor='orange'),
                    ft.ElevatedButton(text='+', color='white', on_click=clicked, data='+')
               ]
          )
          
          fifth_row = ft.Row(
               controls=[
                    ft.ElevatedButton(text='0', color='white', on_click=clicked, data='0', bgcolor='orange', width=120),
                    ft.ElevatedButton(text='.', color='white', on_click=clicked, data='.'),
                    ft.ElevatedButton(text='=', color='white', on_click=equals, data='='),
               ]
          )
     
                   
          self.page.add(
               texter,
               
               first_row,
               second_row,
               third_row,
               fourth_row,
               fifth_row
          )
          
def start():
     ft.app(target=Main)
     
if __name__ == '__main__':
     start()
     