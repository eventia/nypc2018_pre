import turtle as t

def spiral(sp_len):
    while(sp_len >= 5):
        t.forward(sp_len)
        t.right(89)
        sp_len = sp_len - 5

t.speed(0)
spiral(200)
t.hideturtle()
t.done()
