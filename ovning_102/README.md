# �vning 2 - Parametriska kurvor
En parametrisk kurva i planet �r en kurva som definieras av tv� ekvationer. T ex
g�ller f�r en **ellips** 

![](equations/ellipseq.png)

F�r att rita kurvan kan man skapa en lista med en massa tal i intervallet som *t*
ska ligga inom; d�refter s� ber�knas ett *x*- och ett *y*-v�rde f�r varje tal *t*
i listan. Talen *a* och *b* �r godtyckliga, de kommer att best�mma form och
storlek p� ellipsen. Om *a* och *b* �r lika stora kommer figuren att bli en
cirkel (vilket �r ett specialfall av en ellips).

Nedanst�ende bild visar n�gra olika kurvor skapade av parametriska ekvationer,
gjorda i Turtle. F�r att komma ig�ng [finns en startfil](parametriska_kurvor.py)
som ritar ellipsen.

![](./images/parametric_curves.png)

Du ska skapa n�got liknande denna bild med Python och Turtle. H�r �r de
parametriskaekvationerna f�r respektive graf (ellipsen ovan):

### Parabel
![](equations/parabeleq.png)

H�r f�r man pr�va sig fram i vilket intervall *t* ska ligga, det beror p� hur
stor man vill ha parabeln. I exemplet ovan s� �r intervallet mellan -2 och 2.
En kastr�relse i t ex gravitationsf�ltet f�ljer en parabel.

### Hyperbel
![](equations/hyperbeleq.png)

Funktionerna cosh och sinh �r s.k *hyperboliska* funktioner. I Ma4 s� visas dessa
b�da funktioners definitioner och en identitet som kallas den "hyperboliska
ettan" (som liknar den "trigonometriska ettan"). H�r anv�nder vi dem enbart till
att rita grafen som kallas f�r hyperbel.
[H�r kan den som �r intresserad l�sa mer om hyperboliska banor som t ex kometer kan beskriva](https://en.wikipedia.org/wiki/Hyperbolic_trajectory).

### Lemniskata
![](equations/lemniskataeq.png)

Ser ut som en liggande �tta!

### Asteroid
![](equations/asteroideq.png)

Ser lite ut som en stj�rna!


### Descartes l�v
![](equations/descarteseq.png)

Eftersom *t* m�ste vara skilt fr�n 1 f�r man t�nka till hur man ska hantera denna
parametriska ekvation f�r att f� med hela "l�vet" enligt bilden ovan. Ett tips �r
att g�ra tv� intervall, ett som inneh�ller tal som �r mindre �n -2 och ett som
inneh�ller tal st�rre �n -2. Experimentera med s�dana delar.

Man m�rker �ven att vissa delar i l�vet g�r v�ldigt snabbt f�r datorn att rita,
medan andra g�r betydligt l�ngsammare. Det �r inte enbart f�r att det �r tunga
ber�kningar f�r datorn, utan mest f�r att hastigheten ligger i de parametriska
kurvornas natur. Om vi
[plottar derivatan i *x*-led](https://www.wolframalpha.com/input/?i=differentiate+t%2F%281%2Bt%5E3%29)
s� ser vi att den ligger n�ra noll f�r stora belopp p� negativa tal och �ven
stora positiva tal (g�r g�rna motsvarande plot i *y*-led). Derivatan �r ett
m�tt p� hastigheten, s� d�r den ligger n�ra noll kommer ocks� hastigheten p�
uppritningen med denna metod att g�ra det.
 
Rent konkret betyder det att f�r ett och samma intervall (t ex om *t* �kar med
0.1)s� kommer linjen att bli olika l�ng beroende p� var i intervallet vi �r.
N�r derivatan n�rmar sig noll kommer ocks� l�ngden p� den del av linjen som
ritas i intervallet att n�rma sig noll, d�rmed s� g�r det l�ngsammare. Detta
g�ller f�r alla kurvor som ritas genom parametriska ekvationer.
