//ทำให้ user สามารถกำหนด input ได้
extern double PSAR = 0.01;
extern int EMA = 200;
extern double TP = 1;
extern double RISK = 1;
extern int MONEY = 10000;
extern int Magic = 12345;
//สิ้นสุดการ ทำให้ user สามารถกำหนด input ได้
bool state_psarup = 0;
bool state_psardown = 0;
bool laststate_psarup = 0;
bool laststate_psardown = 0;
   
double high = iHigh(NULL,0,1);
double low = iLow(NULL,0,1);
double close = iClose(NULL,0,0);
double open = iOpen(NULL,0,0);
   
double ATR = iATR(NULL,0,14,0);
double P_SAR = iSAR(NULL,0,PSAR,0.2,0);
double periode_sar = iSAR(NULL,0,PSAR,0.2,1);
double E_MA = iMA(NULL,0,200,0,MODE_EMA,PRICE_CLOSE,0);
   
double slatr_buy = NormalizeDouble(low - ATR,Digits);
double slatr_sell = NormalizeDouble(high + ATR,Digits);
   
double lotsizebuy = ((RISK/100) * MONEY) / slatr_buy;
double lotsizesell = ((RISK/100) * MONEY) / slatr_sell;
   
double tp_buy = NormalizeDouble((Ask - slatr_buy) * TP,Digits);
double tp_sell = NormalizeDouble((Bid - slatr_sell) * TP,Digits);
void OnTick() 
{
   int ticket,cntbuy,cntsell;
   
   for (int i = 0; i <= OrdersTotal();i++){
      ticket = OrderSelect(i,SELECT_BY_POS,MODE_TRADES);
      if(OrderSymbol() == Symbol() && OrderMagicNumber() == Magic){
         if(OrderType() == OP_BUY)
         {
            cntbuy++;
         }
         if(OrderType() == OP_SELL)
       {
            cntsell++;
       }
      }
   }

   //PSAR UP
   if(P_SAR < periode_sar && laststate_psarup != 0 && close > E_MA) {
      laststate_psarup != 0;
   }
   //PSAR DOWN
   if(P_SAR > periode_sar && laststate_psarup != 0 && close < E_MA) {
      laststate_psardown != 0;
   }
   //BUY ORDER
   if(cntbuy == 0) {
   if(close > P_SAR && close > E_MA && laststate_psarup == 0) {
      OrderSend(Symbol(),OP_BUY,lotsizebuy,open,0,slatr_buy*Point,tp_buy*Point,NULL,0,0,clrGreen);
      laststate_psarup == 1;
   }
   }
   //SELL ORDER
   if(cntsell == 0) {
   if(close < P_SAR && close < E_MA && laststate_psardown == 0) {
      OrderSend(Symbol(),OP_SELL,lotsizesell,open,0,slatr_sell*Point,tp_sell*Point,NULL,0,0,clrRed);
      laststate_psardown == 1;
   }
   
}
   
   
  
           
         


