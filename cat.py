import turtle

# Pencere ayarları
window = turtle.Screen()
window.bgcolor("black")  # Arka plan siyah
window.title("Kedi Yüzü")

# Kalem ayarları
pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(3)
pen.pensize(5)  # Çizgi kalınlığı artırıldı
pen.color("pink")  # Çizgi rengi pembe

# Kedi yüzü çizimi fonksiyonu
def draw_cat():
    # Kafa
    pen.penup()
    pen.goto(0, -100)
    pen.pendown()
    pen.circle(100)  # Kafa için daire
    
    # Sol göz
    pen.penup()
    pen.goto(-35, 35)
    pen.pendown()
    pen.circle(20)  # Sol göz

    # Sağ göz
    pen.penup()
    pen.goto(35, 35)
    pen.pendown()
    pen.circle(20)  # Sağ göz

    # Burun
    pen.penup()
    pen.goto(0, 15)
    pen.pendown()
    pen.setheading(-60)
    for _ in range(3):
        pen.forward(20)
        pen.left(120)

    # Ağız
    pen.penup()
    pen.goto(-10, -5)
    pen.setheading(-60)
    pen.pendown()
    pen.circle(10, 120)  # Sol taraf
    pen.penup()
    pen.goto(10, -5)
    pen.setheading(-120)
    pen.pendown()
    pen.circle(10, -120)  # Sağ taraf

    # Sol kulak
    pen.penup()
    pen.goto(-75, 80)
    pen.setheading(30)
    pen.pendown()
    pen.forward(50)
    pen.left(120)
    pen.forward(50)

    # Sağ kulak
    pen.penup()
    pen.goto(75, 80)
    pen.setheading(150)
    pen.pendown()
    pen.forward(50)
    pen.right(120)
    pen.forward(50)

# Kedi yüzünü çiz
draw_cat()

# Yazı ekle (kedinin altına)
pen.penup()
pen.goto(0, -150)  # Kedinin altına git
pen.color("pink")  # Yazı rengi pembe
pen.write("Nil", align="center", font=("Arial", 36, "bold"))
pen.hideturtle()

# Pencereyi kapatmamak için
window.mainloop()
