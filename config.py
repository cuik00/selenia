account = {
	"Username":"gondol00",
	"Password":"M1F74H4054$"
}
license = "PLTM-M3G1H-7EK69-AL0E0-MACL5"
tradeset = {
	"BaseTrade":"0.005",
	"C1":"42.12", 					#5-95
	"C2":"45.33", 					#5-95
	"TradeCount":"3", 				#max limit 200
	"MultiplyOnWin":"0", 				## 0 untuk OFF 
	"MultiplyOnLose":"1", 			## 0 untuk OFF 
	"MaxBaseTrade":{
		"Toogle":"OFF",				#ON/OFF
		"Max":"0.001",
		"ResetOnLoseMaxTrade":"OFF", 		# ON/OFF
		"StopOnLoseMaxTrade":"OFF"},		# ON/OFF
	"ClientSeed":"999999",				#max 32 digits
}

tools = {
	"AddDelayTrade":"0",				#Delay Per Trade
	"AddDelayTradeWin":"0",				#Delay Per Trade Win
	"AddDelayTradeLose":"0",			#Delay Per Trade Lose
	"RecoveryMultiplier":"1.5",			# 1 untuk OFF. BaseTrade Lose Terakhir di Kali RecoveryMultiplier
	"RecoveryIncrease":"0",	 			# 0 untuk OFF. BaseTrade Lose Terakhir di Tambah RecoveryIncrease
	"TargetProfit":"100",				#0 untuk OFF
	"StopLoseBalance":"0", 			#0 untuk OFF
	"ForceTC1AfterLose":"ON",			#ON/OFF
	"ChangeTCAfterLose":{
		"Toogle":"ON",
		"ChangeTo":"3"} 			
}
