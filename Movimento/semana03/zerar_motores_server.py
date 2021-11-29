#!/usr/bin/env python3

from __future__ import print_function

from semana02.srv import serv03,serv03Response
import rospy
import random 
import time

def handle_zerar_motores(req):
    req.position = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    rospy.loginfo("Posicoes atuais dos motores:")
    for i in range(20):
        req.position[i] = random.uniform(1.0, 10.0)
        rospy.loginfo("[%s]"%(req.position[i]))
    time.sleep(5)
    rospy.loginfo("Desligando motores, novas posições:")
    for j in range(20):
        req.position[j] = 0
        rospy.loginfo("[%s]"%(req.position[j]))
    return serv03Response(req.position)

def server_zerar_motores():
    rospy.init_node('zerar_motores_server')
    s = rospy.Service('zerar_motores', serv03, handle_zerar_motores)
    print("Pronto para parar os motores")
    rospy.spin()

if __name__ == "__main__":
    server_zerar_motores()