# ICSFinder

## Was macht der ICSFinder?
Es soll mithilfe von SHODAN-Suchanfragen, eingebettet in ein Python-Script, nach 
verfügbaren SCADA-Systemen gesucht werden. Die jeweiligen Ergebnisse sollen 
danach auch auf Erreichbarkeit überprüft werden, daraus soll eine kleine 
Datenbank generiert werden. Die erreichbaren Systeme sollen manuell angesteuert 
werden und Betrachtet werden. Es werden hierbei keinerlei Änderungen am System 
vorgenommen! Es wird lediglich festgestellt, ob das System über einen 
Authentifizierungsmechanismus verfügt ( + Prüfung auf Default-Login) und ob 
Manipulation vorgenommen werden könnte.


