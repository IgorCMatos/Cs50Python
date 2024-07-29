from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar2 = Jar(100)
    assert jar2.capacity == 100
    jar3 = Jar()
    assert jar3.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(11)
    assert jar.size == 12

def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(6)
    assert jar.size == 6
    jar.withdraw(6)
    assert jar.size == 0

