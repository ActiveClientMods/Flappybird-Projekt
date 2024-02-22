# Projekt: Flappybird

# Grading Criteria Programmieren T3INF1004

In jedem Unterbereich werden die Punkte (gerne auch Links ins GIT) erklärt, wie das LO erreicht worden ist.
Alle Kriterien betreffen nur die Projektarbeit. Beweismaterial kommt aus dem Gruppenprojekt.

# FACHKOMPETENZ (40 Punkte)

## Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10)

<!-- Siehe Kenntnisse in prozeduraler Programmierung: zutreffendes wählen und beweisen-->

## Sie können die Syntax und Semantik von Python (10)

<!-- Eine Stelle aus ihrem Programmieren wählen auf die sie besonders stolz sind und begründen -->

![Code für Syntax](https://github.com/ActiveClientMods/Projektarbeit_Flappybird/assets/152853649/69c26d7d-c2e9-494b-bff5-6b136fec5845)
Dieser Ausschnitt definiert eine Klasse "**Bird**" in unter Verwendung der Pygame-Bibliothek. Diese Klasse ist eine Unterklasse von "**pygame.sprite.Sprite**", die eine einfache Basisklasse für sichtbare Spielobjekte in **Pygame** ist.

Die Methode "**\_\_init\_\_**" ist der Konstruktor für die Klasse Bird. Sie nimmt zwei Parameter an, x und y, die die Anfangsposition des Vogels darstellen. Innerhalb des Konstruktors ruft die Zeile "**pygame.sprite.Sprite.\_\_init\_\_(self)**" den Konstruktor der Basisklasse Sprite auf, um sicherzustellen, dass das Bird-Objekt korrekt als Sprite initialisiert wird.

Die Liste "**self.images**" wird initialisiert, um die verschiedenen Bilder zu speichern, die für die Animation des Vogels verwendet werden sollen. Die Variablen "**self.index**" und "**self.counter**" werden auf 0 initialisiert, um zu steuern, welches Bild gerade für den Vogel angezeigt wird, und um den Cooldown zwischen den Bildwechseln zu implementieren.

Die "**for-Schleife**" lädt drei Bilder aus dem Verzeichnis images mit den Namen **bird1.png**, **bird2.png** und **bird3.png** und fügt sie an die Liste "**self.images**" an. Das Attribut self.image wird dann zu Beginn, auf das erste Bild in dieser Liste gesetzt.

Das **self.rect**-Attribut ist ein Pygame Rect-Objekt (Rechteck-Objekt), das für die Kollisionserkennung verwendet wird. Es wird mit den Abmessungen des Bildes initialisiert und sein Mittelpunkt wird auf die dem Konstruktor übergebenen **x**- und **y-Koordinaten** gesetzt. Man kann es sich als eine simple 2D Hitbox im Format eines Recheckes vorstellen.

Die **Update**-Methode wird verwendet, um den Zustand des Vogelobjekts für jedes Bild des Spiels zu aktualisieren. In diesem Fall wird sie verwendet, um die Animation des Vogels zu steuern. Der "**self.counter**" wird bei jedem Aufruf von update um **1** erhöht. Wenn "**self.counter**" den Wert flap_cooldown (der auf 5 gesetzt ist) überschreitet, wird "**self.counter**" auf 0 zurückgesetzt und "**self.index**" um 1 erhöht. "**self.index**" wird verwendet, um die Bilder in der Liste "**self.images**" zu durchlaufen. Wenn "**self.index**" die Länge von "**self.images**" überschreitet, wird er auf 0 zurückgesetzt, was zu einer Schleife der Animation führt. Abschließend wird "**self.image**" auf der Grundlage von "**self.index**" auf das aktuelle Bild gesetzt, wodurch das Aussehen des Vogels aktualisiert wird.

## Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10)

<!-- Anhand von commits zeigen, wie jeder im Projekt einen Beitrag geleistet hat -->
![first-ver](https://github.com/ActiveClientMods/Flappybird-Projekt/assets/152853649/d8ca20d2-c22b-4ad2-a33f-a949f34c0b1d)
![second-ver](https://github.com/ActiveClientMods/Flappybird-Projekt/assets/152853649/cada4594-91f3-4679-9863-edee43924010)
![thrid-ver](https://github.com/ActiveClientMods/Flappybird-Projekt/assets/152853649/82fef6b0-d227-4aba-943b-a9cf35536047)


## Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden. (10)

<!-- Eine Stelle aus dem Projekt wählen auf die sie besonders stolz sind und begründen -->

![datatypes1](https://github.com/ActiveClientMods/Projektarbeit_Flappybird/assets/152853649/54ae006e-bcd6-4cc9-950c-7c79b215d4c1)

Die erste Variable, **white**, ist ein Tupel, das die Farbe Weiß im RGB-Format darstellt. Jeder Wert in dem Tupel kann zwischen 0 und 255 liegen, wobei 0 bedeutet, dass diese Farbe keinen Beitrag leistet und 255 den maximalen Beitrag darstellt. (255, 255, 255) steht also für Weiß.

Die Variable **ground_scroll** wird auf 0 initialisiert und wird verwendet, um das Scrollen des Bodens im Spiel zu steuern. Die Variable scroll_speed ist auf 4 gesetzt und bestimmt die Geschwindigkeit, mit der sich der Boden und die Rohre von rechts nach links bewegen.
Die Variablen center_vertical und center_horizontal werden als die Hälfte von screen_width bzw. screen_height berechnet. Diese Variablen stellen wahrscheinlich den Mittelpunkt des Spielbildschirms dar.

Die Variable **flying** ist ein boolescher Wert, der welcher als Flag dient, um festzustellen, ob der Vogel gerade fliegt. Sie ist zunächst auf False gesetzt, was bedeutet, dass der Vogel zu Beginn des Spiels nicht fliegt.

Die Variable **game_over** ist ein weiterer boolescher Wert, welcher auch als Flag dient und anzeigt, ob das Spiel zu Ende ist. Dieser Wert ist anfangs ebenfalls auf False gesetzt.

Die Variable **pipe_gap** ist auf 150 gesetzt, was den vertikalen Abstand zwischen den oberen und unteren Rohren im Spiel angibt.

Die Variable **pipe_frequency** ist auf 1500 (Millisekunden) gesetzt, was das Zeitintervall zwischen der Erzeugung neuer Rohre darstellt.

Die Variable **last_pipe** wird auf die aktuelle Zeit minus pipe_frequency gesetzt. Damit wird sichergestellt, dass ein neues Rohrpaar erzeugt wird, wenn 1500 vorüber sind, sowie, wenn das Spiel beginnt.

Die **score**-Variable wird auf 0 initialisiert und dient dazu, den Punktestand des Spielers festzuhalten.

Die **pass_pipe**-Variable ist ein weiterer boolescher Wert, der anfangs auf False gesetzt ist. Diese Variable wird verwendet, um zu verfolgen, ob der Vogel ein Rohrpaar erfolgreich durchquert hat.

# METHODENKOMPETENZ (10 Punkte)

## Die Studierenden können eine Entwicklungsumgebung verwenden um Programme zu erstellen (10)

<!-- Beweise anbringen für Nutzen folgender Tools (können links, screenshots und screnncasts sein) -->

<!-- zB -->
<!-- GIT -->
<!-- VSC -->
<!-- Copilot -->
<!-- other -->

### Copilot verwendet, um sich den Code erklären zu lassen

![Use of Copilot1](https://github.com/ActiveClientMods/Projektarbeit_Flappybird/assets/152853649/53b9368c-94cc-4c6c-87c5-3af77a516146)
![Use of Copilot2](https://github.com/ActiveClientMods/Projektarbeit_Flappybird/assets/152853649/793c17bf-73f4-4778-bafa-47b81384fff0)

### Als Entwicklungsumgebung wurde VS Code verwendet.

![use-of-vsc](https://github.com/ActiveClientMods/Projektarbeit_Flappybird/assets/152853649/2cebd952-1a82-4edc-bed9-ff51ddfd6a99)

# PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

## Die Studierenden können ihre Software erläutern und begründen. (5)

<!-- Jeder in der Gruppe: You have helped someone else and taught something to a fellow student (get a support message from one person) -->

## Sie können existierenden Code analysieren und beurteilen. (5)

<!-- Pro Gruppe: You have critiqued another group project. Link to your critique here (another wiki page on your git) and link the project in the critique, use these evaluation criteria to critique the other project. Make sure they get a top grade after making the suggested changes -->

## Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)

<!-- Which technology did you learn outside of the teacher given input -->

Wir lernten unglaublich viel über die Pygame Library. Zuerst hat sie uns komplett erschlagen, doch nach etwas recherche und ein paar YouTube Videos haben wir mit der Zeit immer mehr verstanden.
Auch über das Arbeiten mit VS Code haben wir noch eine Menge neues erfahren.

<!-- Did you or your group get help from someone in the classroom (get a support message here from the person who helped you)
No, we didn't-->

# ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

## Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30)

<!-- Which parts of your project are you proud of and why (describe, analyse, link) -->

Am stolzesten sind wir darauf, dass der Code und somit das Spiel funktioniert.
Wenn wir einen Code-Ausschnitt bestimmen müssen wäre es sehr wahrscheinlich schon der, welcher in "Sie können die Syntax und Semantik von Python (10)" als Screenshot dargestellt ist und erklärt ist.

<!-- Where were the problems with your implementation, timeline, functionality, team management (describe, analyse, reflect from past to future, link if relevant) -->

Anfangs hatten wir kaum Ahnung von Pygame, und wussten nicht recht wie wir das schaffen sollen. Wir hatten viele Überlegungen. Zwischendrin kam sogar die Idee auf, nicht vielleicht doch etwas anderes zu machen. Allerdings legte sich die Krise auch wieder.
Ein großen Problem war die Implementierung der Animation vom Vogel aber auch wie man am effizientesten die ground-scroll Animation.
Schlussendlich haben wir uns für diese Animation des Vogels entschieden, auf welche wir dank eines YT Videos gekommen sind.

Dann blieb nur noch die effiziente ground-scroll Animation das Problem.
Diese haben wir aber letztendlich auch in den Griff bekommen. Zuerst haben wir die ganze Zeit die Pipes generiert und diese wurden nach links mit dem Boden gescrollt. Dabei haben wir gemerkt, dass wir deutliche Leistungseinbußen erleiden. Nach etwas Recherche und ein paar Tagen später sind wir auf die glorreiche Idee gekommen, dass man die Pipes, welche den Screen passiert haben wieder rauslöschen kann und diese somit auch nicht mehr geupdated werden müssen.
Hier ein Screenshot des Codes:

Wenn man dies im Nachhinein sieht, kommt es uns fasst schon lächerlich vor, dass ein If-Statement mit 2 Zeilen eine derartig positive Auswirkung haben kann.

# Kenntnisse in prozeduraler Programmierung:

## - Algorithmenbeschreibung

## - Datentypen

![datatypes1](https://github.com/ActiveClientMods/Projektarbeit_Flappybird/assets/152853649/54ae006e-bcd6-4cc9-950c-7c79b215d4c1)

## - E/A-Operationen und Dateiverarbeitung

![input-screen](https://github.com/ActiveClientMods/Flappybird-Projekt/assets/152853649/477014ae-8b0c-4f22-93a9-e043919e402d)
Unter Eingabe versteht man in unserem Projekt die Maus/Tastatur Eingaben, um den Vogel zum fliegen/sprigen zu bringen.

![output-screen](https://github.com/ActiveClientMods/Flappybird-Projekt/assets/152853649/fa6f904a-7989-45ee-90c1-68f84c8c38a5)
Unter Ausgabe versteht man in unserem Projekt die Ausgabe des Bildes (screen) als grafische Spieloberfläche. 

## - Operatoren

Siehe Funktionen.


## - Kontrollstrukturen
![kontrollstruktur](https://github.com/ActiveClientMods/Flappybird-Projekt/assets/152853649/13892e30-e9ad-4c86-9668-437dc86f3b2d)

## - Funktionen
![function](https://github.com/ActiveClientMods/Flappybird-Projekt/assets/152853649/7cfa1005-ea26-4d65-9e32-2e784b40c424)

## - Stringverarbeitung
![stringverarbeitung](https://github.com/ActiveClientMods/Flappybird-Projekt/assets/152853649/1b849614-a975-43e7-9805-e6b7f3b03239)

## - Strukturierte Datentypen

![datatypes1](https://github.com/ActiveClientMods/Projektarbeit_Flappybird/assets/152853649/54ae006e-bcd6-4cc9-950c-7c79b215d4c1)
