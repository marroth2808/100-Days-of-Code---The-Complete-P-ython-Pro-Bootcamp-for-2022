Start: input = Do you want to play a game of Blackjack? Type 'y' or 'n':
-> Variable game_runs   -> y = True -> next step
                        -> n = False -> stop

logo drucken

array für eigne Karten anlegen
per Zufall Karten aus array cards auswählen 
eignes Kartenarray erweiteren 
aktuellen score und gewählte Karten drucken -> Your cards: [10, 11], current score: 0

array für Computer Karten
Computer zufällige erste Karte geben und drucken -> Computer's first card: 7

Computer weitere zufällige Karte zuteilen 
wenn unter 17 weitere Karte geben -> while
finale Hand und score drucken
Computer's final hand: [7, 10], final score: 17

wenn eigener score < 21 und computer < 21 -> Fragen ob weitere Karte -> input = Type 'y' to get another card, type 'n' to pass: 
zufällig eine Karte auswählen und zuteilen
aktuellen score und gewählte Karten drucken -> Your cards: [10, 11, 10], current score: 0
gewählte Karten und final score anzeigen

sonst gewählte Karten und final score anzeigen -> Karten im eigenen array addieren
Your final hand: [3, 10, 10], final score: 23

final vergleichen
eigner score = 21 -> Blackjack -> Win with a Blackjack 😎
computer score = 21 -> Computer hat Blackjack -> Lose, opponent has Blackjack 😱
eigener score > 21 unddealer_score > 21 -> You went over. You lose 😤
eigener score > 21 -> You went over. You lose 😭
eigener score < computer score -> You lose 😤
computer score > 21 -> Opponent went over. You win 😁
eigener score = computer score -> Draw 🙃
eigener score > computer score -> You win 😃

Rückspul auf Start aber vorherige Eingaben drucken
wenn yes alte Eingaben löschen und neustarten -> while

Kartenasugabe über extra Funktion und jeweils für computer oder user aufrufen
Vergleich auch über extra Funktion

extra Funktion für Summenberechnung

extra Funktion für Festellung ob Blackjack oder Ass
ass durch 1 ersetzen wenn score > 21
wenn Blackjack (score = 21) return 21















