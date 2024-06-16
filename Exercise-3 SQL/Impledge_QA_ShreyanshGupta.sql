--SELECT the details of Doctors(s) who has got Admissions.
SELECT DISTINCT d.doctor_id, d.first_name, d.last_name, d.specialty
FROM doctors d
JOIN admissions a ON d.doctor_id = a.attending_doctor_id;

--SELECT the details of Doctors(s) for whom there is no Admissions.
SELECT d.doctor_id, d.first_name, d.last_name, d.specialty
FROM doctors d
LEFT JOIN admissions a ON d.doctor_id = a.attending_doctor_id
WHERE a.attending_doctor_id IS NULL;


-- SELECT the details of Patients(s) whose Admission can’t be completed due to missing doctor details.
SELECT DISTINCT p.patient_id, p.first_name, p.last_name, p.gender, p.birth_date, p.city, p.province_id, p.allergies, p.height, p.weight
FROM patients p
JOIN admissions a ON p.patient_id = a.patient_id
LEFT JOIN doctors d ON a.attending_doctor_id = d.doctor_id
WHERE d.doctor_id IS NULL;
