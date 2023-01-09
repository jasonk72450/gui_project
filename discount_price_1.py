from guizero import *


def main():
    def calculate():
        try:
            list_price = float(tbx_list_price.value)
            if list_price > 0:
                if tbx_discount_percent.value:
                    discount_percent = float(tbx_discount_percent.value)
                else:
                    discount_percent = 0

                discounted_price = list_price - list_price * discount_percent / 100
                txt_discounted_price.value = f"${discounted_price:.2f}"
            else:
                error(title="Calculator", text="Price must be greater than zero.")
        except ValueError:
            error(title="Calculator", text="You must enter a number.")

    app = App()
    app.text_size = 16

    Text(app, text="List Price")
    tbx_list_price = TextBox(app)

    Box(app, height=30, width=30)
    Text(app, text="Discount Percent")
    tbx_discount_percent = TextBox(app)

    Box(app, height=30, width=30)
    Text(app, text="Discounted Price")
    txt_discounted_price = Text(app, text="$ 0.00")

    Box(app, height=30, width=30)
    PushButton(app, text="Calculate", command=calculate)

    app.display()


if __name__ == '__main__':
    main()
