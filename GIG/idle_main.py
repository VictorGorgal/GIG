try:
    from GUI.idle.idle_gui import Ui_MainWindow
except ModuleNotFoundError:
    from idle_gui import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from time import sleep
from math import floor, log10, sqrt
from shelve import open as sopen
from os import path, getcwd, remove, listdir


class ProgressThread(qtc.QThread):
    change_value = qtc.pyqtSignal(int)

    def __init__(self, time):
        super().__init__()
        self.time = time

    def run(self):
        while True:
            for cnt in range(window.framerate + 1):
                sleep(self.time / window.framerate)
                self.change_value.emit(cnt)


class GoldThread(qtc.QThread):
    change_value = qtc.pyqtSignal(int)

    def run(self):
        sleep(0.01)  # por alguma razao crasha se eu n esperar um pouco (bem pouco)
        while True:
            sleep(1 / window.framerate)
            self.change_value.emit(0)


class OneSecThread(qtc.QThread):
    change_value = qtc.pyqtSignal(int)

    def run(self):
        while True:
            sleep(1)
            self.change_value.emit(0)


class IdleWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        self.starting_gold = 0
        self.gold = self.starting_gold
        self.total_session_gold = self.gold
        self.total_life_gold = self.gold

        self.diamond = 0
        self.total_diamond = self.diamond
        self.diamond_gain = 0
        self.diamond_boost = 0.02
        self.diamond_multiplier = 1

        self.prestiges = 0
        self.framerate = 144
        self.peroption = "bar fill"
        self.to_enable = []
        self.resource_vars_to_save = ["name", "var_name", "total_amount", "amount", "price_base", "price_growth",
                                      "price", "time_base", "time", "progress", "gold_upgrades_multiplier"]
        self.self_vars_to_save = ["starting_gold", "gold", "total_session_gold", "total_life_gold", "diamond",
                                  "total_diamond", "diamond_gain", "diamond_boost", "diamond_multiplier",
                                  "prestiges", "framerate", "peroption", "to_enable"]

        self.rats =     Resource(name="Rats",           var_name="rats",     price=10,    growth=9,   profit=1,     time=1)
        self.flame =    Resource(name="Flame Throwers", var_name="flame",    price=75,    growth=11,  profit=8,     time=2)
        self.slaves =   Resource(name="Slaves",         var_name="slaves",   price=250,   growth=13,  profit=45,    time=3)
        self.machines = Resource(name="Machines",       var_name="machines", price=2e3,   growth=16,  profit=100,   time=4)
        self.chemical = Resource(name="Chemical Bombs", var_name="chemical", price=75e2,  growth=14,  profit=820,   time=5)
        self.yuri =     Resource(name="Yuri",           var_name="yuri",     price=475e2, growth=12,  profit=55e2,  time=6)
        self.hole =     Resource(name="Black Holes",    var_name="hole",     price=213e3, growth=11,  profit=267e2, time=7)
        self.aliens =   Resource(name="Aliens",         var_name="aliens",   price=1e6,   growth=10,  profit=130e3, time=8)
        self.babushka = Resource(name="Babushkas",      var_name="babushka", price=13e7,  growth=9,   profit=175e5, time=9)
        self.soraka =   Resource(name="Sorakas",        var_name="soraka",   price=666e9, growth=7.5, profit=19e10, time=10)

        self.home_button.clicked.connect(lambda: self.pages.setCurrentWidget(self.home))  # page buttons
        self.upgrades_button.clicked.connect(lambda: self.pages.setCurrentWidget(self.upgrades))
        self.diamonds_button.clicked.connect(lambda: self.pages.setCurrentWidget(self.diamonds))
        self.stats_button.clicked.connect(lambda: self.pages.setCurrentWidget(self.stats))
        self.options_button.clicked.connect(lambda: self.pages.setCurrentWidget(self.options))

        self.mine_button.clicked.connect(lambda: self.mine())  # page home
        self.multiplier_button.clicked.connect(lambda: self.multiplier_cycle())
        for stuff in Resource.instances:
            var = stuff.var_name
            getattr(self, f"{var}_button").clicked.connect(getattr(self, var).buy)

        self.rats5x_button.clicked.connect(lambda: self.buy_with_gold("rats5x", 5, "rats", 30))  # page upgrades
        self.flame5x_button.clicked.connect(lambda: self.buy_with_gold("flame5x", 5, "flame", 30))
        self.slaves5x_button.clicked.connect(lambda: self.buy_with_gold("slaves5x", 5, "slaves", 25))
        self.machines5x_button.clicked.connect(lambda: self.buy_with_gold("machines5x", 5, "machines", 25))
        self.chemical5x_button.clicked.connect(lambda: self.buy_with_gold("chemical5x", 5, "chemical", 20))
        self.yuri5x_button.clicked.connect(lambda: self.buy_with_gold("yuri5x", 5, "yuri", 20))
        self.hole5x_button.clicked.connect(lambda: self.buy_with_gold("hole5x", 5, "hole", 15))
        self.aliens5x_button.clicked.connect(lambda: self.buy_with_gold("aliens5x", 5, "aliens", 15))
        self.babushka5x_button.clicked.connect(lambda: self.buy_with_gold("babushka5x", 5, "babushka", 10))
        self.soraka5x_button.clicked.connect(lambda: self.buy_with_gold("soraka5x", 5, "soraka", 10))

        self.diamond1p1_button.clicked.connect(lambda: self.buy_with_gold("diamond1p1", 0.01, "diamond_boost", 10))
        self.diamond1p2_button.clicked.connect(lambda: self.buy_with_gold("diamond1p2", 0.01, "diamond_boost", 10))

        self.everything5x1_button.clicked.connect(lambda: self.buy_with_gold("everything5x1", 5, "diamond_multiplier", 20))
        self.everything5x2_button.clicked.connect(lambda: self.buy_with_gold("everything5x2", 5, "diamond_multiplier", 20))
        self.everything10x_button.clicked.connect(lambda: self.buy_with_gold("everything10x", 10, "diamond_multiplier", 40))

        self.rats2x_button.clicked.connect(lambda: self.buy_with_diamonds("rats2x", 2, "rats", 10))  # page diamonds
        self.flame2x_button.clicked.connect(lambda: self.buy_with_diamonds("flame2x", 2, "flame", 10))
        self.slaves2x_button.clicked.connect(lambda: self.buy_with_diamonds("slaves2x", 2, "slaves", 20))
        self.machines2x_button.clicked.connect(lambda: self.buy_with_diamonds("machines2x", 2, "machines", 20))
        self.chemical2x_button.clicked.connect(lambda: self.buy_with_diamonds("chemical2x", 2, "chemical", 30))
        self.yuri2x_button.clicked.connect(lambda: self.buy_with_diamonds("yuri2x", 2, "yuri", 30))
        self.hole2x_button.clicked.connect(lambda: self.buy_with_diamonds("hole2x", 2, "hole", 40))
        self.aliens2x_button.clicked.connect(lambda: self.buy_with_diamonds("aliens2x", 2, "aliens", 40))
        self.babushka2x_button.clicked.connect(lambda: self.buy_with_diamonds("babushka2x", 2, "babushka", 50))
        self.soraka2x_button.clicked.connect(lambda: self.buy_with_diamonds("soraka2x", 2, "soraka", 60))

        self.starting_gold_100_button.clicked.connect(lambda: self.buy_with_diamonds("starting_gold_100", 100, "starting_gold", 100))
        self.everything2x1_button.clicked.connect(lambda: self.buy_with_diamonds("everything2x1", 2, "diamond_multiplier", 3e3))
        self.everything2x2_button.clicked.connect(lambda: self.buy_with_diamonds("everything2x2", 2, "diamond_multiplier", 25e4))
        self.everything5x_button.clicked.connect(lambda: self.buy_with_diamonds("everything5x", 5, "diamond_multiplier", 1e10))

        self.prestige_button.clicked.connect(lambda: self.prestige())

        self.per_bar_fill_button.clicked.connect(lambda: self.barfill_option())  # page options
        self.save_button.clicked.connect(lambda: self.save())
        self.delete_button.clicked.connect(lambda: self.delete_pending())

        self.delete_confirmation_button.clicked.connect(lambda: self.delete())
        self.close_confirmation_button.clicked.connect(lambda: self.delete_unpending())

        self.goldUpdateStart()
        self.screenUpdateStart()

    def goldUpdateStart(self):  # page 1 functions (home)
        self.gold_thread = GoldThread()
        self.gold_thread.change_value.connect(self.goldUpdate)
        self.gold_thread.start()

    def goldUpdate(self):
        gold_text = f"Gold: {scientify(self.gold)}"
        self.gold_label.setText(gold_text)
        self.diamonds_label.setText(f"Diamonds {scientify(self.diamond)}")

    def screenUpdateStart(self):
        self.update_thread = OneSecThread()
        self.update_thread.change_value.connect(self.screenUpdate)
        self.update_thread.start()

    def screenUpdate(self):
        last_diamond_gain = self.diamond_gain
        self.diamond_gain = 150 * (sqrt(self.total_life_gold) - sqrt(self.total_life_gold - self.total_session_gold)) / 31622776.6
        diamond_per_second = self.diamond_gain - last_diamond_gain

        self.prestige_button.setText(f"Prestige to gain {scientify(self.diamond_gain)} Diamonds (+{scientify(diamond_per_second)} per second)")  # page 3 (diamonds)

        self.total_session_gold_label.setText(f"{scientify(self.total_session_gold)} Gold")  # page 5 (options)
        self.total_life_gold_label.setText(f"{scientify(self.total_life_gold)} Gold")
        self.total_diamonds_label.setText(f"{scientify(self.total_diamond)} Diamonds")
        self.diamond_boost_label.setText(f"{self.diamond_boost * 100}%")
        self.total_prestiges_label.setText(f"{scientify(self.prestiges, decimal_places=0)} Prestiges")

    def mine(self):
        self.gold += 1
        self.total_session_gold += 1
        self.total_life_gold += 1

    def multiplier_cycle(self):
        multiplier_value = self.multiplier_button.text().replace("X", "")
        if multiplier_value == "MA":
            self.multiplier_button.setText("1X")
        elif multiplier_value == "100":
            self.multiplier_button.setText("MAX")
        else:
            self.multiplier_button.setText(f"{int(multiplier_value) * 10}X")

    def buy_with_gold(self, button_name, value, target, price):  # page 2 functions (upgrades)
        self.to_enable.append(f"{button_name}_button")
        if "everything" in button_name or "diamond" in button_name:
            buyable = True
            for stuff in Resource.instances:
                if stuff.amount <= price:
                    buyable = False
            if buyable:
                for stuff in Resource.instances:
                    stuff.amount -= price
                    if "diamond" not in button_name:
                        stuff.gold_upgrades_multiplier *= value
                        stuff.update_time()
                if "diamond" in button_name:
                    self.diamond_boost += value
                getattr(window, f"{button_name}_button").setDisabled(True)
                storage = sopen("./saves/storage")
                storage[f"{button_name}_button"] = True
                storage.close()
        else:
            stuff = getattr(window, target)
            if stuff.amount > price:
                getattr(window, target).amount -= price
                stuff.gold_upgrades_multiplier *= value
                stuff.update_time()
                getattr(window, f"{button_name}_button").setDisabled(True)
                storage = sopen("./saves/storage")
                storage[f"{button_name}_button"] = True
                storage.close()

        self.refresh_resources()

    def buy_with_diamonds(self, button_name, value, target, price):  # page 3 functions (diamonds)
        if self.diamond >= price:
            getattr(window, f"{button_name}_button").setDisabled(True)
            storage = sopen("./saves/storage")
            storage[f"{button_name}_button"] = True
            storage.close()
            self.diamond -= price
            self.diamond_multiplier = 1 + 0.02 * self.diamond

            if "everything" in button_name:
                for stuff in Resource.instances:
                    stuff.profit = stuff.profit * value
            elif "gold" in button_name:
                self.starting_gold += value
            else:
                main_var = target.split(".")[0]
                getattr(window, main_var).profit = getattr(window, main_var).profit * value

            self.refresh_resources()

    def prestige(self):
        if self.diamond_gain >= 1:
            self.diamond += self.diamond_gain
            self.total_diamond += self.diamond_gain
            self.diamond_boost = 0.02
            self.diamond_gain = 0
            self.diamond_multiplier = 1 + self.diamond_boost * self.diamond
            self.gold = self.starting_gold
            self.total_session_gold = self.gold
            self.prestiges += 1

            self.diamonds_label.setText(f"Diamonds: {scientify(self.diamond)}")
            self.prestige_button.setText("Prestige to gain 0.0 Diamonds (+0.0 per second)")

            for resources in Resource.instances:
                try:
                    resources.thread.disconnect()
                except Exception:
                    pass
                resources.amount = 0
                resources.total_amount = 0
                resources.progress = 0
                resources.started = False
                resources.price = resources.price_base
                resources.time = resources.time_base
                resources.gold_upgrades_multiplier = 1
                name = resources.var_name
                getattr(window, f"{name}_progress").setValue(0)
            for button in self.to_enable:
                getattr(window, button).setDisabled(False)
            self.refresh_resources()

    def barfill_option(self):  # page 4 functions (options)
        if self.per_bar_fill_button.text() == "Show gold per bar fill":
            self.per_bar_fill_button.setText("Show gold per second")
            self.peroption = "second"
        else:
            self.per_bar_fill_button.setText("Show gold per bar fill")
            self.peroption = "bar fill"

        self.refresh_resources()

    def refresh_resources(self):
        self.diamond_multiplier = 1 + self.diamond_boost * self.diamond
        for thing in Resource.instances:
            getattr(window, f"{thing.var_name}_label").setText(f"{thing.name}: {scientify(thing.amount, decimal_places=0)}")
            getattr(window, f"{thing.var_name}_button").setText(f"{scientify(thing.price)} Gold")
            diamond_multiplier = self.diamond_multiplier * thing.profit * thing.gold_upgrades_multiplier
            if thing.amount == 0:
                getattr(window, f"{thing.var_name}_profit_label").setText(f"+{scientify(diamond_multiplier)} Gold")
            else:
                if window.peroption == "bar fill":
                    text = f"+{scientify(diamond_multiplier)} Gold (+{scientify(diamond_multiplier * thing.amount)} per bar fill)"
                else:
                    text = f"+{scientify(diamond_multiplier)} Gold (+{scientify(diamond_multiplier * thing.amount / thing.time)} per second)"
                getattr(window, f"{thing.var_name}_profit_label").setText(text)

    def save(self):
        storage = sopen("./saves/storage")
        for stuff in Resource.instances:
            name = stuff.var_name
            for var in self.resource_vars_to_save:
                storage[f"{name}_{var}"] = getattr(stuff, var)

        for var in self.self_vars_to_save:
            storage[f"{var}"] = getattr(self, var)

        storage.close()

    def load(self):
        storage = sopen("./saves/storage")
        for stuff in Resource.instances:
            name = stuff.var_name
            for var in self.resource_vars_to_save:
                setattr(stuff, var, storage[f"{name}_{var}"])
            stuff.started = False

        for var in self.self_vars_to_save:
            setattr(self, var, storage[var])

        for button_key in list(storage.keys()):
            if "button" in button_key:
                getattr(window, f"{button_key}").setDisabled(storage[button_key])

        storage.close()

    def delete_pending(self):
        self.delete_confirmation_button.setDisabled(False)
        self.delete_confirmation_button.setFlat(False)
        self.delete_confirmation_button.setText("Are you sure? The game will delete\nthe current save and will exit")
        self.close_confirmation_button.setDisabled(False)
        self.close_confirmation_button.setText("x")

    def delete_unpending(self):
        self.delete_confirmation_button.setText("")
        self.delete_confirmation_button.setDisabled(True)
        self.delete_confirmation_button.setFlat(True)
        self.close_confirmation_button.setText("")
        self.close_confirmation_button.setDisabled(True)

    def delete(self):
        for file_name in listdir(f"{getcwd()}/saves"):
            remove(f"{getcwd()}/saves/{file_name}")
        exit()


class Resource:
    instances = []

    def __init__(self, name, var_name, price, growth, profit, time):
        self.name = name
        self.var_name = var_name
        self.total_amount = 0
        self.amount = 0
        self.price_base = price
        self.price_growth = 1 + growth / 100
        self.price = price
        self.profit_base = profit
        self.profit = profit
        self.time_base = time
        self.time = time
        self.progress = 0
        self.gold_upgrades_multiplier = 1
        self.started = False
        self.instances.append(self)

    def set(self):
        getattr(window, f"{self.var_name}_button").setText(f"{scientify(self.price)} Gold")
        getattr(window, f"{self.var_name}_profit_label").setText(f"+{scientify(self.profit)} Gold")
        getattr(window, f"{self.var_name}_progress").setMaximum(window.framerate)

        if not self.started and self.amount > 0:
            self.started = True
            self.startProgress()

    def buy(self):
        gold = window.gold
        multiplier_text = window.multiplier_button.text().replace("X", "")
        if multiplier_text == "MA":
            multiplier_value = max(floor(log10((gold * (self.price_growth - 1) / self.price) + 1) / log10(self.price_growth)), 1)
        else:
            multiplier_value = int(multiplier_text)
        price = self.price * (self.price_growth ** multiplier_value - 1) / (self.price_growth - 1)

        if gold >= price:
            if not self.started:
                self.started = True
                self.startProgress()
            window.gold -= price
            self.amount += multiplier_value
            self.total_amount += multiplier_value
            self.price = self.price_base * self.price_growth ** self.total_amount
            self.update_time()
            window.refresh_resources()

    def startProgress(self):
        self.thread = ProgressThread(self.time)
        self.thread.change_value.connect(self.progressThread)
        self.thread.start()

    def progressThread(self, val):
        if self.time > 0.33:
            getattr(window, f"{self.var_name}_progress").setValue(val)
        else:
            getattr(window, f"{self.var_name}_progress").setValue(window.framerate)
        if val == window.framerate:
            profit = self.profit * self.amount * self.gold_upgrades_multiplier * window.diamond_multiplier
            window.gold += profit
            window.total_session_gold += profit
            window.total_life_gold += profit

    def update_time(self):
        self.time = self.time_base * 0.97265 ** (self.amount - 1)
        if self.time < 0.33:
            self.time = 0.33
        self.thread.time = self.time


def scientify(number, decimal_places=2):
    if number >= 1000:
        number = format(number, "1.2e").replace("+0", '').replace("+", "")
    else:
        if decimal_places == 0:
            number = floor(number)
        else:
            number = floor(number * 10 ** decimal_places) / 10 ** decimal_places
    return number


if __name__ == '__main__':
    app = qtw.QApplication([])

    window = IdleWindow()
    file_path = f"{getcwd()}/saves/storage.bak"
    if path.isfile(file_path):
        window.load()
    for resource in Resource.instances:
        resource.set()
    window.refresh_resources()
    window.show()
    app.exec_()
    window.save()
