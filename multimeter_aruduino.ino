// this is a voltage(current)meter for zlac motor which has the maximum of (24v,30A)
// also measure power distributor'(abbrievated by PD below)s voltage and current(24V,30A)

#define SSR_VOLTAGE_ANALOG_IN_PIN A0
#define SSR_CURRENT_ANALOG_IN_PIN A1

#define PD_VOLTAGE_ANALOG_IN_PIN A5
#define PD_CURRENT_ANALOG_IN_PIN A4

//this part is for SSR output voltage parameter
float vout_ssr = 0.0;
float vin_ssr = 0.0; 
float R1 = 100000.0; //anode side:R1(100K)
float R2 = 10000.0; //cathode side:R2(10K)
int vvalue_voltage_ssr = 0; //analog read value

//this part is for PD voltage parameter
float vout_pd = 0.0;
float vin_pd = 0.0; 
int vvalue_voltage_pd = 0; //analog read value

//this part is for SSR output current parameter
float sensitivity_ssr = 0.066; //(V/A) ELC30
float offsetvoltage_ssr = 2.5; //calibration!!!
int vvalue_current_ssr = 0; //analog read value
double currentmetervoltage_ssr = 0;
double cin_ssr = 0;

//this part is for pd current parameter
float sensitivity_pd = 0.066; //(V/A) ELC30
float offsetvoltage_pd = 2.5; //calibration!!!
int vvalue_current_pd = 0; //analog read value
double currentmetervoltage_pd = 0;
double cin_pd = 0;

//time
unsigned long starttime;
unsigned long currenttime;
const unsigned long period = 100; //10mHz

void setup(){
	//setup serial 
	Serial.begin(9600);
	Serial.println("start measuring");
	Serial.println("time(s)/PD(V)/SSR(V)/PD(A)/SSR(A)");

	//time
	starttime = millis(); //initial start time
}

void loop(){
	//time
	currenttime = millis();
	
	if (currenttime - starttime >= period)
	{
	//time display
	Serial.print(millis()/1000.0, 2);
	Serial.print(" ");	

	//pd voltage
	vvalue_voltage_pd = analogRead(PD_VOLTAGE_ANALOG_IN_PIN);
	vout_pd = (vvalue_voltage_pd * 5.0) / 1024.0; //seperate 5V to 1024 pieces
	vin_pd = vout_pd / (R2/(R1+R2)); //cathode side voltage is what we want
	if (abs(vin_pd)<0.09){
	vin_pd = 0.0; //statement to quash undesired reading!
	}
	
	//pd voltage display
	char voltage_pd[20];
	char voltagevalue_pd[10];
	dtostrf(vin_pd, 5, 2, voltagevalue_pd);
	sprintf(voltage_pd, "%05s ", voltagevalue_pd);
	Serial.print(voltage_pd);
	Serial.print(" ");	
	
	//ssr voltage
	vvalue_voltage_ssr = analogRead(SSR_VOLTAGE_ANALOG_IN_PIN);
	vout_ssr = (vvalue_voltage_ssr * 5.0) / 1024.0; //seperate 5V to 1024 pieces
	vin_ssr = vout_ssr / (R2/(R1+R2)); //cathode side voltage is what we want
	if (abs(vin_ssr)<0.09){
	vin_ssr = 0.0; //statement to quash undesired reading!
	}
	
	//pd voltage display
	char voltage_ssr[20];
	char voltagevalue_ssr[10];
	dtostrf(vin_ssr, 5, 2, voltagevalue_ssr);
	sprintf(voltage_ssr, "%05s ", voltagevalue_ssr);
	Serial.print(voltage_ssr);
	Serial.print(" ");	
	
	//pd current
	vvalue_current_pd = analogRead(PD_CURRENT_ANALOG_IN_PIN); 
	currentmetervoltage_pd = (vvalue_current_pd / 1024.0) * 5; 
	cin_pd = ((currentmetervoltage_pd - offsetvoltage_pd) / sensitivity_pd);
	if (abs(cin_pd)<0.1){
	cin_pd = 0.0;
	}

	//pd current display
	char current_pd[20];
	char currentvalue_pd[10];
	dtostrf(cin_pd, 5, 2, currentvalue_pd);
	sprintf(current_pd, "%05s", currentvalue_pd);	
	Serial.print(current_pd);
	Serial.print(" ");	
	
	//ssr current
	vvalue_current_ssr = analogRead(SSR_CURRENT_ANALOG_IN_PIN); 
	currentmetervoltage_ssr = (vvalue_current_ssr / 1024.0) * 5; 
	cin_ssr = ((currentmetervoltage_ssr - offsetvoltage_ssr) / sensitivity_ssr);
	if (abs(cin_ssr)<0.1){
	cin_ssr = 0.0;
	}

	//ssr current display
	char current_ssr[20];
	char currentvalue_ssr[10];
	dtostrf(cin_ssr, 5, 2, currentvalue_ssr);
	sprintf(current_ssr, "%05s", currentvalue_ssr);	
	Serial.print(current_ssr);
	Serial.println("");

	starttime = currenttime;
	}
}



	
