-- Identify potentially fraudulent claims based on abnormal patterns
SELECT patient_id, claim_id, claim_amount, claim_date, 
       heart_rate, oxygen_level, temperature,
       CASE 
           WHEN heart_rate > 110 OR oxygen_level < 90 OR temperature > 102 THEN 'Potential Fraud'
           ELSE 'Normal'
       END AS fraud_risk
FROM healthcare_claims
WHERE claim_amount > (SELECT AVG(claim_amount) * 2 FROM healthcare_claims)
ORDER BY fraud_risk DESC, claim_amount DESC;
