-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT *
FROM crime_scene_reports
WHERE month = 7 AND day = 28;

SELECT *
FROM interviews
WHERE year = 2025 AND month = 7 AND day = 28 AND id > 160 AND id < 191;

SELECT *
FROM atm_transactions a
JOIN bank_accounts b ON a.account_number = b.account_number
JOIN people p ON b.person_id = p.id
WHERE a.atm_location = 'Leggett Street' AND a.month = 7 AND a.day = 28 AND a.year = 2025
GROUP BY a.account_number;

SELECT *
FROM bakery_security_logs b
JOIN people p ON b.license_plate = p.license_plate
WHERE year = 2025 AND month = 7 AND day = 28 AND hour = 10 AND minute > 15 AND minute < 30 AND b.activity = 'exit';



SELECT p2.name, p.flight_id, f.destination_airport_id, f.hour, f.minute, a2.city, b.license_plate
FROM airports a
JOIN flights f ON a.id = f.origin_airport_id
JOIN airports a2 ON a2.id = f.destination_airport_id
JOIN passengers p ON f.id = p.flight_id
JOIN people p2 ON p.passport_number = p2.passport_number
JOIN bakery_security_logs b ON p2.license_plate = b.license_plate
WHERE a.abbreviation = 'CSF' AND f.month = 7 AND f.day = 29 AND f.hour < 12
GROUP BY p2.name
ORDER BY f.hour asc;

SELECT *
FROM phone_calls
WHERE month = 7 AND day = 28 AND year = 2025 AND caller = '(367) 555-5533';

SELECT *
FROM people
WHERE phone_number = '(375) 555-8161';
