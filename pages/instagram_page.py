import unittest
from appium import webdriver
import time 
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait

class instagram_page():

    def __init__(self, driver):
        self.driver = driver
        self.seguindo = ''
        self.seguidores = ''
        self.contador = 1
        self.contador_2 = 0

    def ir_ate_o_seguidor_escolhido(self, usuario_para_seguir):
        self.driver.implicitly_wait(1000)
        e = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextSwitcher/android.widget.TextView')
        e.click()
        e = self.driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="Perfil"]/android.widget.ImageView')
        e.click()
        try:
            e = self.driver.find_element_by_id('com.instagram.android:id/profile_header_following_count')
            e.click()
        except:
            e = self.driver.find_element_by_id('com.instagram.android:id/row_profile_header_textview_following_count')   
            e.click()
            pass 
        e = self.driver.find_element_by_id('com.instagram.android:id/row_search_edit_text').send_keys('{}'.format(usuario_para_seguir))
        e = self.driver.find_element_by_id('com.instagram.android:id/follow_list_username').click()
        e = self.driver.find_element_by_id('com.instagram.android:id/profile_header_followers_count').click()





    def seguir(self):
        
        self.contador_2 = 0
        self.contador = 1
        
        while(self.contador_2 != 12):
            for usuario in range(2, 6):
                try:
                    print("ENTREIN E TENTEI ACHAR")
                    el = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[{}]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]'.format(usuario))
                    print("PASSOU AQUIII")                                                                           
                    el3 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[{}]/android.widget.LinearLayout/android.widget.TextView'.format(usuario))
                    el3 = el3.text
                    print(el3)
                        
                    if(el3 != 'Seguindo' and el3 != 'Solicitado'):

                        print('O CONTADOR ESTÁ NO {}'.format(self.contador)) 
                        print("O USUARIO eh o numero {}".format(usuario))                   
                        print('O Nome do usuairo eh {}'.format(el.text))

                        if(el.text != ''):
                            actions = TouchAction(self.driver)
                            actions.tap(el)
                            actions.perform()
                            seguidores = self.driver.find_element_by_id('com.instagram.android:id/profile_header_followers_count')   
                            seguindo = self.driver.find_element_by_id('com.instagram.android:id/profile_header_following_count')

                            self.seguidores = seguidores.text
                            self.seguindo = seguindo.text
                    #-----------------------------Algoritmo de limpeza de inteiros-------
                            print("MEU SELF SEGUIDORES ESTá assim {}  e meu SELF SEGUINDO esta assim {}".format(self.seguidores, self.seguindo))
                            self.limpar_algoritmos()
                    #--------------------------------------------------------------------
                            print(self.seguidores)
                            print(self.seguindo)
                            ja_seguindo_1 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]')
                            
                            print('O JA SEGUINDO ESTA RECEBENDO {}'.format(ja_seguindo_1.text))
                            if(ja_seguindo_1.text != 'Mensagem' and ja_seguindo_1.text != 'Solicitado' and ja_seguindo_1.text != 'Seguir de volta' ):    
                                if(int(self.seguindo) > int(self.seguidores)):
                                    print("ESTA ENTRANDO NA VALIDACAO DE INTEIROS")
                                    self.armazenar_no_txt()
                                    self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]').click()
                                    self.driver.back()
                                else:
                                    self.driver.back()
                                    self.contadores_1_2(self.contador, self.contador_2)
                            else:
                                self.driver.back()
                                self.contadores_1_2(self.contador, self.contador_2)                            
                        else:
                            pass         
                    else:
                        self.contadores_1_2(self.contador, self.contador_2)
                        pass
                except:
                    print("TO CAINDO AQUI")
                    assert 2 == 1
                    pass

    def limpar_algoritmos(self):

        print("SEGUIDORES {} SEGUINDO {}".format(self.seguidores, self.seguindo))
        
        self.seguidores = self.seguidores.replace('Seguidores', '') 
        self.seguidores = ''.join(self.seguidores)

        self.seguindo = self.seguindo.replace('Seguindo', '')
        self.seguindo = ''.join(self.seguindo)

        print('Meus seguidores sao {} e meus seguindo sao {} '.format(self.seguidores,self.seguindo))

        if('.' in self.seguidores): 
            self.seguidores = list(filter(lambda palavra: '.' not in palavra ,  self.seguidores))
            self.seguidores = ''.join(self.seguidores)
            if('mil' in self.seguidores):
                self.seguidores = self.seguidores.replace('mil', '000')
            elif('mi' in self.seguidores):
                self.seguidores = self.seguidores.replace('mi', '000')    
            else:
                pass
        else:
            pass 
        
         
        if('.' in self.seguindo):   
            self.seguindo = list(filter(lambda palavra: '.' not in palavra ,  self.seguindo))
            self.seguindo = ''.join(self.seguindo)
            if('mil' in self.seguindo):
                self.seguindo = self.seguindo.replace('mil', '000')
            elif('mi' in self.seguindo):
                self.seguindo = self.seguindo.replace('mi', '000')    
            else:
                pass
        else:
            pass 
        
        if(',' in self.seguidores):
            self.seguidores = list(filter(lambda palavra: ',' not in palavra ,  self.seguidores))
            self.seguidores = ''.join(self.seguidores)
            if('mil' in self.seguidores):
                self.seguidores = self.seguidores.replace('mil', '00')
            elif('mi' in self.seguidores):
                self.seguidores = self.seguidores.replace('mi', '00000')           
            else:
                pass
        else:
            pass

        if(',' in self.seguindo):
            self.seguindo = list(filter(lambda palavra: ',' not in palavra ,  self.seguindo))
            self.seguindo = ''.join(self.seguindo)
            if('mil' in self.seguindo):                    
                self.seguindo = self.seguindo.replace('mil', '00')
            elif('mi' in self.seguindo):
                self.seguindo = self.seguindo.replace('mi', '00000')    
            else:
                pass
        else:
            pass        
        if(' ' in self.seguindo):
            self.seguindo = list(filter(lambda palavra: ' ' not in palavra ,  self.seguindo))      
            self.seguindo = ''.join(self.seguindo)
            if('mil' in self.seguindo):
                self.seguindo = self.seguindo.replace('mil', '000')
            elif('mi' in self.seguindo):
                self.seguindo = self.seguindo.replace('mi', '00000')    
            else:
                pass
        else:
            pass        
        if(' ' in self.seguidores):
            self.seguidores = list(filter(lambda palavra: ' ' not in palavra ,  self.seguidores))            
            self.seguidores = ''.join(self.seguidores)
            if('mil' in self.seguidores):                    
                self.seguidores = self.seguidores.replace('mil', '000')
            elif('mi' in self.seguidores):
                self.seguidores = self.seguidores.replace('mi', '00000')    
            else:
                pass                
        else:
            pass 
           
        
        
        
        
        print("SEGUINDORES = {} SEGUINDO = {}".format(self.seguidores, self.seguindo))
        self.seguidores = list(filter(lambda palavra: ' ' not in palavra ,  self.seguidores))
        self.seguindo = list(filter(lambda palavra: ' ' not in palavra ,  self.seguindo))
        self.seguidores = ''.join(self.seguidores)
        self.seguindo = ''.join(self.seguindo)
                            
    def armazenar_no_txt(self):

        e = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView')
        e = e.text
                        
        file_ = open('Seguidos.txt', 'r')
        conteudo_txt = file_.readlines()                
        conteudo_txt.append('\n'+e)
        file_.close()

        file_ = open('Seguidos.txt', 'w')
        file_.writelines(conteudo_txt)
        file_.close()
    
    def contadores_1_2(self, contador, contador_2):
        if(contador == 4):
            TouchAction(self.driver).press(x=429, y=1719).move_to(x=450, y=420).release().perform()
            self.contador = 1
            self.contador_2 = contador_2 + 1 
        else:
            self.contador = contador + 1

# TEM TODOS OS 4 botoes dentro '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]'   se acrescentar /android.widget.TextView[1] entra no s        
# tem os dois botoes de cima   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]'
# Tem os layouts 2 botoe baixo '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]'
