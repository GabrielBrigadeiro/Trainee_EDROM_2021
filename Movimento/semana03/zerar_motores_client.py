#!/usr/bin/env python

from __future__ import print_function
import rospy
from semana02.srv import *


def zerar_motores_client(pos):
    rospy.wait_for_service('zerar_motores')
    pos_motores = [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    id_motores = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    torq_motores = [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True]
    try:
        parar_motores = rospy.ServiceProxy('zerar_motores', serv03)
        resp1 = parar_motores(id_motores,pos_motores,torq_motores)
        printar_resultado(id_motores,pos_motores,torq_motores)  
        return resp1.resposta
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
      

def printar_resultado(id,position,torque):
    for i in range (20):
        print("ID: %i, Posicao: %f, Torque: %r"%(id[i],position[i],torque[i]))
        

if __name__ == "__main__":
    pos = 0
    zerar_motores_client(pos)