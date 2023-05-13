import datetime
import os, sys
import re
import sqlite3
from kivy.config import Config
from kivy.lang import Builder
from kivymd.app import MDApp, App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.resources import resource_add_path
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.taptargetview import MDTapTargetView
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import ScrollView
from kivymd.uix.card import MDCard
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp
from kivy.uix.tabbedpanel import TabbedPanel
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.core.window import Window
from kivymd.uix.fitimage import FitImage
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDIconButton
from kivymd.uix.textfield import MDTextField
import mysql.connector as mysql_conn
from PIL import Image
from kivy.uix.widget import Widget
from kivy.clock import Clock
import tempfile
from kivy.factory import Factory

Clock.max_iteration = 30
Config.set("graphics", "resizable", 0)
# Builder.load_file("VibelyAppDes.kv")


class Likes_List(MDCard):
    pass


class CategMDCard(MDCard):
    pass


class CardElementMDCard(MDCard):
    pass


class LoginMDTextField(MDTextField):
    pass


class RegisMDTextField(MDTextField):
    pass


class ALLCateg(MDCard):
    pass


class MyIconButton(MDIconButton):
    pass


########################################################################
class Tab(FloatLayout, MDTabsBase):
    pass


class Scroller(ScrollView):
    pass


class MyTab(FloatLayout, MDTabsBase):
    pass


########################################################################
class LikesCard(MDCard):
    pass


class ProfileMDCard(MDCard):
    pass


class MyTabPanel(TabbedPanel):
    pass


############################################################################################


class SuccessRegistration(MDDialog, MDFloatLayout):
    pass


class FailRegistration(MDDialog, MDFloatLayout):
    pass


class vibelyApp(MDBoxLayout):
    # def update_image(self, carousel, index):
    #     current_image_index = index

    # def load_next(self,allimage,current_image_index):
    #     if len(allimage) > 0:
    #         current_image_index = (self.current_image_index + 1) % len(allimage)
    #         self.ids.addtoBL.add_widget(CategMDCard(FitImage(source=allimage[current_image_index])))
    #         self.current_image_index = current_image_index
    #         Clock.schedule_once(self.load_next, 5)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Window.bind(on_keyboard=self.events) ### still figuring out why this is necessary
        # self.manager_open = True
        
        global user_id
        user_id = None
        # self.set_list
        # self.refresh_callback
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager, select_path=self.select_path
        )

        conn = mysql_conn.connect(
            host="vibelyapp.cxuua18zjocr.ap-southeast-2.rds.amazonaws.com",
            user="admin",
            passwd="vibelyPassword",
            database="vibelyApp",
        )
        sqli3conn = sqlite3.connect(
            "C:/Users/Mark Francis/Documents/School/ITPE02/KIVY_DEV/aaVibely/new/DATABASES/kivyDatabase.db",
            detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
        )

        cursor = conn.cursor()
        cursor.execute("""SELECT name FROM Movies""")
        rowsMovies = [", ".join(map(str, row)) for row in cursor.fetchall()]
        cursor = conn.cursor()
        cursor.execute("""SELECT name FROM Foods""")
        rowsFoods = [", ".join(map(str, row)) for row in cursor.fetchall()]
        cursor = conn.cursor()
        cursor.execute("""SELECT name FROM Songs""")
        rowsSongs = [", ".join(map(str, row)) for row in cursor.fetchall()]
        cursor = conn.cursor()
        cursor.execute("""SELECT name FROM Sports""")
        rowsSports = [", ".join(map(str, row)) for row in cursor.fetchall()]
        cursor = conn.cursor()
        cursor.execute("""SELECT name FROM Games""")
        rowsGames = [", ".join(map(str, row)) for row in cursor.fetchall()]
        
        import io
        from base64 import b64encode
        from kivy.core.image import Image as CoreImage
        # cursor.execute(
        #     """SELECT * FROM usersFavorite WHERE userID =  %s""",
        #     (user_id,),
        # )
        # all_to_show = [", ".join(map(str, row)) for row in cursor.fetchall() if None not in row]
        # self.images=[]
        # for row in all_to_show:
        #     cursor.execute(
        #     "SELECT image FROM Games WHERE name = :name",
        #     {"name": row},
        # )
        #     image_data = cursor.fetchone()[0]
        #     data = io.BytesIO(image_data)
        #     im = CoreImage(data, ext="png").texture
        #     #self.ids.addtoBL.add_widget(CategMDCard(FitImage(source=im)))
        #     self.images.append(im)
        # current_image_index = 0
        # self.load_next( self.images,current_image_index)
        # self.bind(,index=self.update_image)
        # getFavGames
        # getFavGames
        c = conn.cursor()
        for movie in rowsMovies:
            cur = sqli3conn.cursor()
            cur.execute(
                "SELECT image FROM Movies WHERE name = ?",
                (movie,),
            )
            image_data = cur.fetchone()[0]
            data = io.BytesIO(image_data)

            # Load PNG image using Kivy
            im = CoreImage(data, ext="png").texture
            # print(im)
            fit = FitImage(
                source=im,
                radius=16,
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
            add_fav = MDIconButton(
                id=movie,
                icon="heart-outline",
                pos_hint={"center_x": 0.85, "center_y": 0.15},
            )
            add_fav.bind(on_release=self.getFavMovies)
            box = MDFloatLayout()
            card = ALLCateg(id=movie)
            box.add_widget(fit)
            box.add_widget(add_fav)
            card.add_widget(box)
            self.ids.StackOfMovies.add_widget(card)
            # cur.execute(
            #     "SELECT name FROM Movies WHERE name = ?",
            #     (str(add_fav.id),),
            # )
        for game in rowsGames:
            cur = sqli3conn.cursor()
            cur.execute(
                "SELECT image FROM Games WHERE name = ?",
                (game,),
            )
            image_data = cur.fetchone()[0]

            data = io.BytesIO(image_data)
            # print(data)
            im = CoreImage(data, ext="png").texture
            # print(im)
            fit = FitImage(
                source=im,
                radius=16,
                
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
            add_fav = MDIconButton(
                id=game,
                icon="heart-outline",
                pos_hint={"center_x": 0.85, "center_y": 0.15},
            )
            add_fav.bind(on_release=self.getFavGames)
            box = MDFloatLayout()
            card = ALLCateg(id=game)
            box.add_widget(fit)
            box.add_widget(add_fav)
            card.add_widget(box)
            self.ids.StackOfGames.add_widget(card)
            # cur.execute(
            #     "SELECT name FROM Games WHERE name =  ?",
            #     (str(add_fav.id),),
            # )
        for song in rowsSongs:
            cur = sqli3conn.cursor()
            cur.execute(
                "SELECT image FROM Songs WHERE name = ?",
                (song,),
            )
            image_data = cur.fetchone()[0]

            data = io.BytesIO(image_data)
            # print(data)
            im = CoreImage(data, ext="png").texture
            # print(im)
            fit = FitImage(
                source=im,
                radius=16,
                
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
            add_fav = MDIconButton(
                id=song,
                icon="heart-outline",
                pos_hint={"center_x": 0.85, "center_y": 0.15},
            )
            add_fav.bind(on_release=self.getFavSongs)
            box = MDFloatLayout()
            card = ALLCateg(id=song)
            box.add_widget(fit)
            box.add_widget(add_fav)
            card.add_widget(box)
            self.ids.StackOfSongs.add_widget(card)
            # cur.execute(
            #     "SELECT name FROM Songs WHERE name =  ?",
            #     (str(add_fav.id),),
            # )
        for sport in rowsSports:
            cur = sqli3conn.cursor()
            cur.execute(
                "SELECT image FROM Sports WHERE name = ?",
                (sport,),
            )
            image_data = cur.fetchone()[0]

            data = io.BytesIO(image_data)
            # print(data)
            im = CoreImage(data, ext="png").texture
            # print(im)
            fit = FitImage(
                source=im,
                radius=16,
                
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
            add_fav = MDIconButton(
                id=sport,
                icon="heart-outline",
                pos_hint={"center_x": 0.85, "center_y": 0.15},
            )
            add_fav.bind(on_release=self.getFavSports)
            box = MDFloatLayout()
            card = ALLCateg(id=sport)
            box.add_widget(fit)
            box.add_widget(add_fav)
            card.add_widget(box)
            self.ids.StackOfSports.add_widget(card)
            # cur.execute(
            #     "SELECT name FROM Sports WHERE name = ?",
            #     (str(add_fav.id),),
            # )
        for food in rowsFoods:
            cur = sqli3conn.cursor()
            cur.execute(
                "SELECT image FROM Foods WHERE name = :name",
                (food,),
            )
            image_data = cur.fetchone()[0]

            data = io.BytesIO(image_data)
            # print(data)
            im = CoreImage(data, ext="png").texture
            # print(im)
            fit = FitImage(
                source=im,
                radius=16,
                
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
            add_fav = MDIconButton(
                id=food,
                icon="heart-outline",
                pos_hint={"center_x": 0.85, "center_y": 0.15},
            )
            add_fav.bind(on_release=self.getFavFoods)
            box = MDFloatLayout()
            card = ALLCateg(id=food)
            box.add_widget(fit)
            box.add_widget(add_fav)
            card.add_widget(box)
            self.ids.StackOfFoods.add_widget(card)
            # cur.execute(
            #     "SELECT name FROM Foods WHERE name = ?",
            #     (str(add_fav.id),),
            # )

        conn.commit()
        conn.close()
        sqli3conn.commit()
        sqli3conn.close()
    def home(self, id_clicked):
        conn = mysql_conn.connect(
            host="vibelyapp.cxuua18zjocr.ap-southeast-2.rds.amazonaws.com",
            user="admin",
            passwd="vibelyPassword",
            database="vibelyApp",
        )
        cur = conn.cursor()
        sqli3conn = sqlite3.connect(
            "C:/Users/Mark Francis/Documents/School/ITPE02/KIVY_DEV/aaVibely/new/DATABASES/kivyDatabase.db",
            detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
        )
        cursql = sqli3conn.cursor()

        self.ids.home_container.clear_widgets()

        import io
        from base64 import b64encode
        from kivy.core.image import Image as CoreImage
        if id_clicked == "movieshome":
            
            cur.execute(
            """SELECT movies FROM usersFavorite WHERE userID =  %s""",
            (user_id,),
        )
            

            rows = [", ".join(map(str, row)) for row in cur.fetchall() if None not in row]
        
            self.ids.home_container.clear_widgets()
            
            # create new MDCardAgents widgets for each agent
            for movies in rows:
                cursql.execute(
                    "SELECT image FROM Movies WHERE name = ?",
                    (movies,),
                )
                cur.execute(
                "SELECT description,genre,length,year,title FROM Movies WHERE name = %s",
                (movies,),
            )
                rows = cur.fetchall()
                movie_des = rows[0][0]
                movie_genre = rows[0][1]
                movie_length = rows[0][2]
                movie_year = rows[0][3]
                movie_title = rows[0][4]
                image_data = cursql.fetchone()[0]
                data = io.BytesIO(image_data)
                im = CoreImage(data, ext="png").texture

                card = Factory.MDCardHome()
                card.ids.title_mdcard.text = movie_title
                card.ids.year_mdcard.text = str(movie_year)
                card.ids.about_mdcard.text = movie_des
                card.ids.image_mdcard.source = im

                self.ids.home_container.add_widget(card)
            conn.commit()
            sqli3conn.commit()
            conn.close()
            sqli3conn.close()

            
        elif id_clicked == "gameshome":
            cur.execute(
            """SELECT games FROM usersFavorite WHERE userID =  %s""",
            (user_id,),
        )
            

            rows = [", ".join(map(str, row)) for row in cur.fetchall() if None not in row]

            self.ids.home_container.clear_widgets()
            
            # create new MDCardAgents widgets for each agent
            for row in rows:
                cursql.execute(
                "SELECT image FROM Games WHERE name = :name",
                {"name": row},
            )
                image_data = cursql.fetchone()[0]
                data = io.BytesIO(image_data)
                im = CoreImage(data, ext="png").texture
                cur.execute(
                    "SELECT description,date,type,title FROM Games WHERE name = %s",
                    (row,),
                )
                rows = cur.fetchall()
                game_des = rows[0][0]
                game_date = rows[0][1]
                game_type = rows[0][2]
                game_name = rows[0][3]

                card = Factory.MDCardHome()
                card.ids.title_mdcard.text = game_name
                card.ids.year_mdcard.text = str(game_date)
                card.ids.about_mdcard.text = game_des
                card.ids.image_mdcard.source = im

                self.ids.home_container.add_widget(card)

            conn.commit()
            sqli3conn.commit()
            conn.close()
            sqli3conn.close()

        elif id_clicked == "songhome":
            cur.execute(
            """SELECT music FROM usersFavorite WHERE userID =  %s""",
            (user_id,),
        )
            

            rows = [", ".join(map(str, row)) for row in cur.fetchall() if None not in row]

        
            self.ids.home_container.clear_widgets()


            # create new MDCardAgents widgets for each agent
            for song in rows:
                cursql.execute(
                "SELECT image FROM Songs WHERE name = :name",
                {"name":song},
            )
                image_data = cursql.fetchone()[0]
                data = io.BytesIO(image_data)
                im = CoreImage(data, ext="png").texture
                cur.execute(
                    "SELECT writers,duration,singer,lyrics,title FROM Songs WHERE name = %s",(song,),)
                
                rows = cur.fetchall()
                song_writer = rows[0][0]
                song_dur = rows[0][1]
                song_singer = rows[0][2]
                song_lyrics = rows[0][3]
                song_title = rows[0][4]

                card = Factory.MDCardHome()
                card.ids.title_mdcard.text = song_title
                card.ids.year_mdcard.text = song_writer
                card.ids.about_mdcard.text = song_singer #Create another column in songs (About the song)
                card.ids.image_mdcard.source = im

                self.ids.home_container.add_widget(card)

            conn.commit()
            sqli3conn.commit()
            conn.close()
            sqli3conn.close()
            
        elif id_clicked == "foodhome":
            cur.execute(
            """SELECT food FROM usersFavorite WHERE userID =  %s""",
            (user_id,),
        )
            

            rows = [", ".join(map(str, row)) for row in cur.fetchall() if None not in row]

        
            self.ids.home_container.clear_widgets()

            # create new MDCardAgents widgets for each agent
            for food in rows:
                cursql.execute(
                "SELECT image FROM Foods WHERE name = :name",
                {"name": food},
            )
                image_data = cursql.fetchone()[0]
                data = io.BytesIO(image_data)
                im = CoreImage(data, ext="png").texture
                cur.execute(
                    "SELECT description,ingredient,steps,title FROM Foods WHERE name = %s",
                    (food,),
                )
                rows = cur.fetchall()
                food_des = rows[0][0]
                food_ing = rows[0][1]
                food_steps = rows[0][2]
                food_title = rows[0][3]



                card = Factory.MDCardHome()
                card.ids.title_mdcard.text = food_title
                card.ids.year_mdcard.text = 'Food' #Create another column in database ("What kind ")
                card.ids.about_mdcard.text = food_des
                card.ids.image_mdcard.source = im

                self.ids.home_container.add_widget(card)

            conn.commit()
            sqli3conn.commit()
            conn.close()
            sqli3conn.close()

        elif id_clicked == "sporthome":
            cur.execute(
            """SELECT sports FROM usersFavorite WHERE userID =  %s""",
            (user_id,),
        )
            

            rows = [", ".join(map(str, row)) for row in cur.fetchall() if None not in row]

        
            self.ids.home_container.clear_widgets()

            # create new MDCardAgents widgets for each agent
            for sport in rows:
                cursql.execute(
                "SELECT image FROM Sports WHERE name = :name",
                {"name": sport},
            )

                image_data = cursql.fetchone()[0]
                data = io.BytesIO(image_data)
                im = CoreImage(data, ext="png").texture
                cur.execute(
                    "SELECT description,origin,title FROM Sports WHERE name = %s",
                    (sport,),
                )
                rows = cur.fetchall()
                sport_des = rows[0][0]
                sport_or = rows[0][1]
                sport_title = rows[0][2]

                card = Factory.MDCardHome()
                card.ids.title_mdcard.text = sport_title
                card.ids.year_mdcard.text = sport_or
                card.ids.about_mdcard.text = sport_des
                card.ids.image_mdcard.source = im

                self.ids.home_container.add_widget(card)

            conn.commit()
            sqli3conn.commit()
            conn.close()
            sqli3conn.close()
    def all_of_movies(self, user_num):
        self.to_get_fav(
            """SELECT movies FROM usersFavorite WHERE userID =  %s""",
            "SELECT image FROM Movies WHERE name = :name",
            "movie",
            user_num,
        )

    def all_of_games(self, user_num):
        self.to_get_fav(
            """SELECT games FROM usersFavorite WHERE userID = %s""",
            "SELECT image FROM Games WHERE name = :name",
            "game",
            user_num,
        )

    def all_of_songs(self, user_num):
        self.to_get_fav(
            """SELECT music FROM usersFavorite WHERE userID =  %s""",
            "SELECT image FROM Songs WHERE name = :name",
            "song",
            user_num,
        )

    def all_of_foods(self, user_num):
        self.to_get_fav(
            """SELECT food FROM usersFavorite WHERE userID =  %s""",
            "SELECT image FROM Foods WHERE name = :name",
            "food",
            user_num,
        )

    def all_of_sports(self, user_num):
        self.to_get_fav(
            """SELECT sports FROM usersFavorite WHERE userID =  %s""",
            "SELECT image FROM Sports WHERE name = :name",
            "sport",
            user_num,
        )

    _bool_ = None

    def fav_clicked(self):
        self.all_of_movies(user_id)
        self.all_of_games(user_id)
        self.all_of_songs(user_id)
        self.all_of_foods(user_id)
        self.all_of_sports(user_id)

    def to_get_fav(self, select, get_image, cat_id, user_num):
        import io
        from base64 import b64encode
        from kivy.core.image import Image as CoreImage

        conn = mysql_conn.connect(
            host="vibelyapp.cxuua18zjocr.ap-southeast-2.rds.amazonaws.com",
            user="admin",
            passwd="vibelyPassword",
            database="vibelyApp",
        )
        sqli3conn = sqlite3.connect(
            "C:/Users/Mark Francis/Documents/School/ITPE02/KIVY_DEV/aaVibely/new/DATABASES/kivyDatabase.db",
            detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
        )
        cur = conn.cursor()
        cur.execute(
            select,
            (user_num,),
        )
        rows = [", ".join(map(str, row)) for row in cur.fetchall() if None not in row]
        if cat_id == "movie":
            cur.execute(
                select,
                (user_num,),
            )
            rows = [
                ", ".join(map(str, row)) for row in cur.fetchall() if None not in row
            ]
            for row in rows:
                c = sqli3conn.cursor()
                c.execute(
                    get_image,
                    {"name": row},
                )
                image_data = c.fetchone()[0]
                data = io.BytesIO(image_data)
                im = CoreImage(data, ext="png").texture
                fit = FitImage(
                    source=im,
                    radius=7,
                    size=(self.width, self.height),
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )

                box = MDFloatLayout()
                var1 = "movie"
                card = Likes_List(
                    id=row,
                    on_release=lambda card, var1=var1: self.details_button_all(
                        card, var1
                    ),
                    
                )
                box.add_widget(fit)
                card.add_widget(box)
                self.ids.all_my_movies.add_widget(card)
        elif cat_id == "game":
            cur.execute(
                select,
                (user_num,),
            )
            rows = [
                ", ".join(map(str, row)) for row in cur.fetchall() if None not in row
            ]
            for row in rows:
                c = sqli3conn.cursor()
                c.execute(
                    get_image,
                    {"name": row},
                )
                image_data = c.fetchone()[0]
                data = io.BytesIO(image_data)
                im = CoreImage(data, ext="png").texture
                fit = FitImage(
                    source=im,
                    radius=7,
                    size=(self.width, self.height),
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                """clicked = MDIconButton(
                    id=movie,
                    icon="heart-outline",
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                add_fav.bind(on_release=self.clicked)"""
                box = MDFloatLayout()
                var1 = "game"
                card = Likes_List(
                    id=row,
                    on_release=lambda card, var1=var1: self.details_button_all(
                        card, var1
                    ),
                    
                )
                box.add_widget(fit)
                card.add_widget(box)
                self.ids.all_my_games.add_widget(card)
        elif cat_id == "song":
            cur.execute(
                select,
                (user_num,),
            )
            rows = [
                ", ".join(map(str, row)) for row in cur.fetchall() if None not in row
            ]
            for row in rows:
                c = sqli3conn.cursor()
                c.execute(
                    get_image,
                    {"name": row},
                )
                image_data = c.fetchone()[0]
                data = io.BytesIO(image_data)
                im = CoreImage(data, ext="png").texture
                fit = FitImage(
                    source=im,
                    radius=7,
                    size=(self.width, self.height),
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )

                box = MDFloatLayout()
                var1 = "song"
                card = Likes_List(
                    id=row,
                    on_release=lambda card, var1=var1: self.details_button_all(
                        card, var1
                    ),
                    
                )
                box.add_widget(fit)
                card.add_widget(box)
                self.ids.all_my_songs.add_widget(card)
        elif cat_id == "food":
            cur.execute(
                select,
                (user_num,),
            )
            rows = [
                ", ".join(map(str, row)) for row in cur.fetchall() if None not in row
            ]
            for row in rows:
                c = sqli3conn.cursor()
                c.execute(
                    get_image,
                    {"name": row},
                )
                image_data = c.fetchone()[0]
                data = io.BytesIO(image_data)
                im = CoreImage(data, ext="png").texture
                fit = FitImage(
                    source=im,
                    radius=7,
                    size=(self.width, self.height),
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )

                box = MDFloatLayout()
                var1 = "food"
                card = Likes_List(
                    id=row,
                    on_release=lambda card, var1=var1: self.details_button_all(
                        card, var1
                    ),
                    
                )

                box.add_widget(fit)
                card.add_widget(box)
                self.ids.all_my_foods.add_widget(card)
        else:
            cur.execute(
                select,
                (user_num,),
            )
            rows = [
                ", ".join(map(str, row)) for row in cur.fetchall() if None not in row
            ]
            for row in rows:
                c = sqli3conn.cursor()
                c.execute(
                    get_image,
                    {"name": row},
                )
                image_data = c.fetchone()[0]
                data = io.BytesIO(image_data)
                im = CoreImage(data, ext="png").texture
                fit = FitImage(
                    source=im,
                    radius=7,
                    size=(self.width, self.height),
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )

                box = MDFloatLayout()
                var1 = "sport"
                get_id = row
                card = Likes_List(
                    id=row,
                    on_release=lambda card, var1=var1: self.details_button_all(
                        card, var1
                    ),
                   
                )
                global sport_card
                sport_card = card.id
                box.add_widget(fit)
                card.add_widget(box)
                self.ids.all_my_sports.add_widget(card)
        conn.commit()
        conn.close()
        sqli3conn.commit()
        sqli3conn.close()

    def returnScreen(self, screen, direct):
        self.ids.detailScreen.current = screen
        self.ids.detailScreen.transition.direction = direct

    def details_button_all(self, all_card_id, type_id):
        print("IDDSSS >>>>>  ", all_card_id.id)
        conn = mysql_conn.connect(
            host="vibelyapp.cxuua18zjocr.ap-southeast-2.rds.amazonaws.com",
            user="admin",
            passwd="vibelyPassword",
            database="vibelyApp",
        )
        sqli3conn = sqlite3.connect(
            "C:/Users/Mark Francis/Documents/School/ITPE02/KIVY_DEV/aaVibely/new/DATABASES/kivyDatabase.db",
            detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
        )
        import io
        from base64 import b64encode
        from kivy.core.image import Image as CoreImage

        cur = conn.cursor()
        c = sqli3conn.cursor()
        if type_id == "movie":
            self.ids.detailScreen.current = "gotomovie"
            self.ids.detailScreen.transition.direction = "left"

            c.execute(
                "SELECT image FROM Movies WHERE name = :name",
                {"name": all_card_id.id},
            )
            image_data = c.fetchone()[0]
            data = io.BytesIO(image_data)
            im = CoreImage(data, ext="png").texture
            cur.execute(
                "SELECT description,genre,length,year,title FROM Movies WHERE name = %s",
                (str(all_card_id.id),),
            )
            rows = cur.fetchall()
            movie_des = rows[0][0]
            movie_genre = rows[0][1]
            movie_length = rows[0][2]
            movie_year = rows[0][3]
            movie_title = rows[0][4]
            self.ids.fitthemovie.source = im
            self.ids.movie_title.text = str(movie_title.upper())
            self.ids.movie_det.text = f"Description :\n\n\t     {movie_des}\n\n\nGenre : {movie_genre}\n\nReleased year : {movie_year}\n\nDuration : {movie_length}"

        elif type_id == "game":
            self.ids.detailScreen.current = "gotogame"
            self.ids.detailScreen.transition.direction = "left"
            c.execute(
                "SELECT image FROM Games WHERE name = :name",
                {"name": all_card_id.id},
            )
            image_data = c.fetchone()[0]
            data = io.BytesIO(image_data)
            im = CoreImage(data, ext="png").texture
            cur.execute(
                "SELECT description,date,type,title FROM Games WHERE name = %s",
                (str(all_card_id.id),),
            )
            rows = cur.fetchall()
            game_des = rows[0][0]
            game_date = rows[0][1]
            game_type = rows[0][2]
            game_name = rows[0][3]
            self.ids.fitthegame.source = im
            self.ids.game_name.text = str(game_name.upper())
            self.ids.game_des.text = f"Description :\n\n\t{game_des}\n\nRelease Date : {game_date}\n\nType : {game_type}"
        elif type_id == "song":
            self.ids.detailScreen.current = "gotosong"
            self.ids.detailScreen.transition.direction = "left"

            c.execute(
                "SELECT image FROM Songs WHERE name = :name",
                {"name": all_card_id.id},
            )
            image_data = c.fetchone()[0]
            data = io.BytesIO(image_data)
            im = CoreImage(data, ext="png").texture
            cur.execute(
                "SELECT writers,duration,singer,lyrics,title FROM Songs WHERE name = %s",
                (str(all_card_id.id),),
            )
            rows = cur.fetchall()
            song_writer = rows[0][0]
            song_dur = rows[0][1]
            song_singer = rows[0][2]
            song_lyrics = rows[0][3]
            song_title = rows[0][4]
            self.ids.fitthesong.source = im
            self.ids.song_title.text = str(song_title.upper())
            self.ids.song_det.text = f"Writer : {song_writer}\n\nSinger : {song_singer}\nDuration : {song_dur}\n\nLyrics :\n\n{song_lyrics}"
        elif type_id == "food":
            self.ids.detailScreen.current = "gotofood"
            self.ids.detailScreen.transition.direction = "left"
            c.execute(
                "SELECT image FROM Foods WHERE name = :name",
                {"name": all_card_id.id},
            )
            image_data = c.fetchone()[0]
            data = io.BytesIO(image_data)
            im = CoreImage(data, ext="png").texture
            cur.execute(
                "SELECT description,ingredient,steps,title FROM Foods WHERE name = %s",
                (str(all_card_id.id),),
            )
            rows = cur.fetchall()
            food_des = rows[0][0]
            food_ing = rows[0][1]
            food_steps = rows[0][2]
            food_title = rows[0][3]
            self.ids.fitthefood.source = im
            self.ids.food_title.text = str(food_title.upper())
            self.ids.food_det.text = f"Description :\n\n{food_des}\n\n\Ingredient : {food_ing}\n\Steps :\n\n{food_steps}"
        elif type_id == "sport":
            self.ids.detailScreen.current = "gotosport"
            self.ids.detailScreen.transition.direction = "left"
            c.execute(
                "SELECT image FROM Sports WHERE name = :name",
                {"name": all_card_id.id},
            )

            image_data = c.fetchone()[0]
            data = io.BytesIO(image_data)
            im = CoreImage(data, ext="png").texture
            cur.execute(
                "SELECT description,origin,title FROM Sports WHERE name = %s",
                (str(all_card_id.id),),
            )
            rows = cur.fetchall()
            sport_des = rows[0][0]
            sport_or = rows[0][1]
            sport_title = rows[0][2]

            self.ids.fitthesport.source = im
            self.ids.sport_title.text = str(sport_title.upper())
            self.ids.sport_det.text = (
                f"Description :\n\n{sport_des}\n\nOrigin : {sport_or}"
            )
        conn.commit()
        conn.close()
        sqli3conn.commit()
        sqli3conn.close()

    def movieScreen(self, screen, direct):
        self.ids.categScreen.current = screen
        self.ids.categScreen.transition.direction = direct

    def gameScreen(self, screen, direct):
        self.ids.categScreen.current = screen
        self.ids.categScreen.transition.direction = direct

    def songScreen(self, screen, direct):
        self.ids.categScreen.current = screen
        self.ids.categScreen.transition.direction = direct

    def sportScreen(self, screen, direct):
        self.ids.categScreen.current = screen
        self.ids.categScreen.transition.direction = direct

    def foodScreen(self, screen, direct):
        self.ids.categScreen.current = screen
        self.ids.categScreen.transition.direction = direct

    def travelScreen(self, screen, direct):
        self.ids.categScreen.current = screen
        self.ids.categScreen.transition.direction = direct

    def getFavMovies(self, add_fav):
        self._bool_ = None
        conn = mysql_conn.connect(
            host="vibelyapp.cxuua18zjocr.ap-southeast-2.rds.amazonaws.com",
            user="admin",
            passwd="vibelyPassword",
            database="vibelyApp",
        )

        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM Movies WHERE name = %s",
            (str(add_fav.id),),
        )
        name = cursor.fetchone()[0]
        cursor.execute(
            """SELECT movies FROM usersFavorite WHERE userID = %s""",
            (user_id,),
        )
        rows = [", ".join(map(str, row)) for row in cursor.fetchall()]
        if name not in rows:
            cursor.execute(
                "INSERT INTO usersFavorite(userID,movies)VALUES(%s,%s)",
                (
                    user_id,
                    name,
                ),
            )
            self.refresh_callback()
            # print("naprint sya ",user_id)
        self.commit_conn(add_fav, conn)

    def getFavGames(self, add_fav):
        self._bool_ = None
        conn = mysql_conn.connect(
            host="vibelyapp.cxuua18zjocr.ap-southeast-2.rds.amazonaws.com",
            user="admin",
            passwd="vibelyPassword",
            database="vibelyApp",
        )
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM Games WHERE name = %s",
            (str(add_fav.id),),
        )
        name = cursor.fetchone()[0]
        cursor.execute(
            """SELECT games FROM usersFavorite WHERE userID = %s""",
            (user_id,),
        )
        rows = [", ".join(map(str, row)) for row in cursor.fetchall()]
        if name not in rows:
            cursor.execute(
                "INSERT INTO usersFavorite(userID,games)VALUES(%s,%s)",
                (
                    user_id,
                    name,
                ),
            )
            self.refresh_callback()
        self.commit_conn(add_fav, conn)

    def getFavSongs(self, add_fav):
        self._bool_ = None
        conn = mysql_conn.connect(
            host="vibelyapp.cxuua18zjocr.ap-southeast-2.rds.amazonaws.com",
            user="admin",
            passwd="vibelyPassword",
            database="vibelyApp",
        )
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM Songs WHERE name = %s",
            (str(add_fav.id),),
        )
        name = cursor.fetchone()[0]
        cursor.execute(
            """SELECT music FROM usersFavorite WHERE userID = %s""",
            (user_id,),
        )
        rows = [", ".join(map(str, row)) for row in cursor.fetchall()]
        if name not in rows:
            cursor.execute(
                "INSERT INTO usersFavorite(userID,music)VALUES(%s,%s)",
                (
                    user_id,
                    name,
                ),
            )
            self.refresh_callback()
        self.commit_conn(add_fav, conn)

    def getFavSports(self, add_fav):
        self._bool_ = None
        conn = mysql_conn.connect(
            host="vibelyapp.cxuua18zjocr.ap-southeast-2.rds.amazonaws.com",
            user="admin",
            passwd="vibelyPassword",
            database="vibelyApp",
        )
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM Sports WHERE name = %s",
            (str(add_fav.id),),
        )
        name = cursor.fetchone()[0]
        cursor.execute(
            """SELECT sports FROM usersFavorite WHERE userID = %s""",
            (user_id,),
        )
        rows = [", ".join(map(str, row)) for row in cursor.fetchall()]
        if name not in rows:
            cursor.execute(
                "INSERT INTO usersFavorite(userID,sports)VALUES(%s,%s)",
                (
                    user_id,
                    name,
                ),
            )
            self.refresh_callback()
        self.commit_conn(add_fav, conn)

    def getFavFoods(self, add_fav):
        self._bool_ = None
        conn = mysql_conn.connect(
            host="vibelyapp.cxuua18zjocr.ap-southeast-2.rds.amazonaws.com",
            user="admin",
            passwd="vibelyPassword",
            database="vibelyApp",
        )
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM Foods WHERE name = %s",
            (str(add_fav.id),),
        )
        name = cursor.fetchone()[0]
        cursor.execute(
            """SELECT food FROM usersFavorite WHERE userID = %s""",
            (user_id,),
        )
        rows = [", ".join(map(str, row)) for row in cursor.fetchall()]
        if name not in rows:
            cursor.execute(
                "INSERT INTO usersFavorite(userID,food)VALUES(%s,%s)",
                (
                    user_id,
                    name,
                ),
            )
            self.refresh_callback()
           
        self.commit_conn(add_fav, conn)

    # TODO Rename this here and in `getFavMovies`, `getFavGames`, `getFavSongs`, `getFavSports` and `getFavFoods`
    def commit_conn(self, add_fav, conn):
        add_fav.icon = "heart"
        conn.commit()
        conn.close()

    def build(self):
        self.load_movies()

    def set_list(self):
        from kivymd.utils import asynckivy

        async def set_list():
            self.all_of_movies(user_id)
            self.all_of_games(user_id)
            self.all_of_songs(user_id)
            self.all_of_foods(user_id)
            self.all_of_sports(user_id)

        asynckivy.start(set_list())

    _bool_ = None

    def refresh_callback(self):
        """A method that updates the state of your application
        while the spinner remains on the screen."""
        if self._bool_ is None:

            def refresh_callback(interval):
                self.ids.all_my_games.clear_widgets()
                self.ids.all_my_movies.clear_widgets()
                self.ids.all_my_sports.clear_widgets()
                self.ids.all_my_songs.clear_widgets()
                self.ids.all_my_foods.clear_widgets()
                self.set_list()

            self._bool_ = "FALSE"
            Clock.schedule_once(refresh_callback, 0)

    '''def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"'''

    """def file_manager_open(self):
        self.file_manager.show(os.path.expanduser("~"))  # output manager to the screen
        self.manager_open = True"""

    ############################################################################################
    def select_path(self, path: str):
        """
        It will be called when you click on the file name
        or the catalog selection button.

        :param path: path to the selected directory or file;
        """
        self.exit_manager()
        global profile
        # print(self.add())
        # self.myprofilePic(path)
        if "profile" in get_path:
            mycard = ProfileMDCard(FitImage(source=path))
            self.ids.put_on_FL.add_widget(mycard)
            toast("Succesfully Changed Profile")
            return path

        # if self.add == "clicked":
        elif "add album" in get_path:
            mycard = LikesCard(FitImage(source=path))
            self.ids.addtoBL.add_widget(mycard)
            toast("Succesfully added to album")

    # def profile(self, path_profile):
    #     conn = mysql_conn.connect(
    #         host="vibelyapp.cxuua18zjocr.ap-southeast-2.rds.amazonaws.com",
    #         user="admin",
    #         passwd="vibelyPassword",
    #         database="vibelyApp",
    #     )
    #     cursor = conn.cursor()

    #     cursor.execute(
    #         """
    #     CREATE TABLE IF NOT EXISTS profile_pictures
    #     (name TEXT)"""
    #     )
    #     cursor.execute(
    #         "INSERT INTO profile_pictures(name) VALUES (:name)",
    #         {"name": path_profile},
    #     )
    #     conn.commit()
    #     # cursor.close()
    #     conn.close()

    ############################################################################################
    def exit_manager(self, *args):
        """Called when the user reaches the root of the directory tree."""
        self.manager_open = True
        self.file_manager.close()
        return True

    ############################################################################################
    ### dont know yet why this is necessary,,, it makes my other button being click
    '''def events(self, instance, keyboard, keycode, text, modifiers):
        """Called when buttons are pressed on the mobile device."""
        if keyboard in (1001, 27) and self.manager_open:
            self.file_manager.back()
        return True'''

    ############################################################################################
    def myprofilePic(self):
        self.get_the_clicked_button("profile")

    def add(self):
        self.get_the_clicked_button("add album")

    ############################################################################################
    # TODO Rename this here and in `myprofilePic` and `add`
    def get_the_clicked_button(self, button):
        self.file_manager.show(os.path.expanduser("~"))
        self.manager_open = True
        global get_path
        get_path = [button]

    ############################################################################################

    def to_signin(self, screen, direction):
        self.ids.manager.current = screen
        self.ids.manager.transition.direction = direction

    def to_signup(self, screen, direction):
        self.ids.manager.current = screen
        self.ids.manager.transition.direction = direction

    def logout(self, *args):
        # Functionality for item 3
        self.ids.manager.current = "loginScreen"
        self.ids.manager.transition.direction = "right"

    # action__________-------------------------

    # Light Theme

    def to_regisScreen(self, screenName, direction):
        self.ids.manager.current = screenName
        self.ids.manager.animation_type = direction

    def returnToLog(self, screenName, direction):
        self.ids.manager.current = screenName
        self.ids.manager.transition.direction = direction

    def signin(self):
        us = self.ids.username.text
        p = self.ids.passw.text
        dbconn = mysql_conn.connect(
            host="vibelyapp.cxuua18zjocr.ap-southeast-2.rds.amazonaws.com",
            user="admin",
            passwd="vibelyPassword",
            database="vibelyApp",
        )
        c = dbconn.cursor()
        c.execute(
            "SELECT * FROM Registered_User WHERE Registered_User.username = %s and Registered_User.password = %s",
            (
                us,
                p,
            ),
        )
        if record := c.fetchall():
            self.logged(c, us, p)
            self.ids.the_username.text = record[0][1]
            self.ids.the_email.secondary_text = record[0][2]
            self.ids.the_type.secondary_text = record[0][6]
            if self._bool_ is None:

                def signin(interval):
                    self.ids.all_my_games.clear_widgets()
                    self.ids.all_my_movies.clear_widgets()
                    self.ids.all_my_sports.clear_widgets()
                    self.ids.all_my_songs.clear_widgets()
                    self.ids.all_my_foods.clear_widgets()
                    self.set_list()

                self._bool_ = "FALSE"
                Clock.schedule_once(signin, 0)
        else:
            FailRegistration().open()
        dbconn.commit()
        dbconn.close()

    # TODO Rename this here and in `signin`
    def logged(self, c, us, p):
        self.ids.manager.current = "inVibely"
        self.ids.manager.transition.direction = "left"
        self.ids.username.text = ""
        self.ids.passw.text = ""
        c.execute(
            "SELECT * FROM Registered_User WHERE Registered_User.username = %s and Registered_User.password = %s",
            (
                us,
                p,
            ),
        )
        global user_id
        user_id = c.fetchone()[0]

        print(user_id)
    def validate_password(self, password):
        if len(password) < 8:
            self.root.ids.regisPass.error = True
        else:
            self.root.ids.regisPass.error = False
    def is_valid_username(self,username):
        regex = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]+$'
        return bool(re.match(regex, username))
    def is_valid_email(self,email):
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(regex, email))
    def SuccessRegis(self):
        check = [
            self.ids.regisUser.text,
            self.ids.regisEmail.text,
            self.ids.regisPass.text,
        ]
        global pop
        pop = "Registered Successfully" if "" not in check and self.is_valid_username(self.ids.regisUser.text) and self.is_valid_email( self.ids.regisEmail.text)  else "Incomplete Requirements"
        if pop == "Registered Successfully":
            SuccessRegistration().open()
            self.insertData()
        else:
            FailRegistration().open()
        # self.insertData()
        return pop

    def insertData(self):
        dbconn = mysql_conn.connect(
            host="vibelyapp.cxuua18zjocr.ap-southeast-2.rds.amazonaws.com",
            user="admin",
            passwd="vibelyPassword",
            database="vibelyApp",
        )
        c = dbconn.cursor()
        usern = self.ids.regisUser.text
        email = self.ids.regisEmail.text
        password = self.ids.regisPass.text
        c.execute(
            "INSERT INTO Registered_User(username, email, password, created_at, updated_at)VALUES(%s, %s, %s, %s, %s)",
            (
                usern,
                email,
                password,
                datetime.datetime.now(),
                datetime.datetime.now(),
            ),
        )
        dbconn.commit()
        dbconn.close()

    def messageLog(self, popM):
        messagePOP = self.message2(popM)
        messagePOP.open()

    def message2(self, popM):
        box = BoxLayout()
        box.orientation = "vertical"
        box.add_widget(Label(text=popM))
        button = Button(
            text="OK",
            background_color=(201 / 255, 44 / 255, 109 / 255, 0.5),
            background_normal="",
        )
        box.add_widget(button)
        result = Popup(
            title="",
            content=box,
            size_hint=(0.5, 0.25),
            auto_dismiss=False,
            background_color=(31 / 255, 138 / 255, 112 / 255, 0.8),
        )
        button.bind(on_release=result.dismiss)
        return result

    ############################----------THEME----------#######################################################
    def LDtheme(self, app):
        if app.theme_cls.theme_style == "Light":
            self.Dark(app)
        else:
            self.Light(app)

    def Light(self, app):
        app.theme_cls.theme_style = "Light"
        app.theme_cls.primary_palette = "Indigo"

    # Dark Theme
    def Dark(self, app):
        app.theme_cls.theme_style = "Dark"
        app.theme_cls.primary_palette = "DeepPurple"


##################################----------THEME----------#################################################


    def search(self):
        # get text from search_input
        search_text = self.ids.search_input.text

        # connect to the database
        conn = sqlite3.connect('C:/Users/Mark Francis/Documents/School/ITPE02/KIVY_DEV/aaVibely/new/DATABASES/kivyDatabase.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
        )
        c = conn.cursor()

        # retrieve data from table1
        c.execute("SELECT title FROM search WHERE title LIKE ?", ('%'+search_text+'%',))

        import io
        from base64 import b64encode
        from kivy.core.image import Image as CoreImage

        self.ids.search_list.clear_widgets()
        spacing_widget = Widget(size_hint_y=None, height = 30)
        self.ids.search_list.add_widget(spacing_widget)
        results= [", ".join(map(str, row)) for row in c.fetchall()]
        print(results)
        for result in results:
            
            cur = conn.cursor()
            cur.execute(
                "SELECT image FROM search WHERE title = ?",
                (result,),
            )
            image_data = cur.fetchone()[0]
            data = io.BytesIO(image_data)

            # Load PNG image using Kivy
            im = CoreImage(data, ext="png").texture
            
            
            list = Factory.Search_Result()
            list.height= dp(200)
            list.text_list = result
            list.ids.search_pic.source = im
            list.bind(on_release= lambda instance: self.details_button_all(instance.content_id))
            self.ids.search_list.add_widget(list)        
            
            
        # ###############3
    

        
        


        conn.close()


# Designate Our .kv design file


class screenManagerApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.accent_palette = "Red"
        self.theme_cls.primary_hue = "900"

        return vibelyApp()


if __name__ == "__main__":
    if hasattr(sys, "_MEIPASS"):
        resource_add_path(os.path.join(sys._MEIPASS))
    screenManagerApp().run()
