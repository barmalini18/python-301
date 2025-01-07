from toga import App, MainWindow, Button

class MyApp(App):
    def startup(self):
        self.main_window = MainWindow(title="My App")
        self.main_window.content = Button("Hello")
        self.main_window.show()

if __name__ == "__main__":
    MyApp("My App", "org.beeware.demo").main_loop()