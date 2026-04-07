import * as fs from 'fs';

function generateData() {
    const rows = 500;
    const header = "previous_marks,attendance_percentage,study_hours_per_day,assignment_score,internal_marks,extracurricular_participation,internet_usage_hours,parents_education_level,family_income,final_exam_score\n";
    let csvContent = header;

    for (let i = 0; i < rows; i++) {
        const prev_marks = (Math.random() * 60 + 40).toFixed(1);
        const attendance = (Math.random() * 40 + 60).toFixed(1);
        const study_hours = (Math.random() * 10 + 1).toFixed(1);
        const assignment = (Math.random() * 50 + 50).toFixed(1);
        const internal = (Math.random() * 30 + 20).toFixed(1);
        const extra = Math.random() > 0.7 ? 1 : 0;
        const internet = (Math.random() * 8 + 1).toFixed(1);
        const parents_edu = Math.floor(Math.random() * 3) + 1;
        const income = (Math.random() * 8000 + 2000 + parents_edu * 1000).toFixed(2);

        // Target calculation with correlations
        let score = 15;
        score += parseFloat(prev_marks) * 0.2;
        score += parseFloat(attendance) * 0.1;
        score += parseFloat(study_hours) * 3.0;
        score += parseFloat(assignment) * 0.15;
        score += parseFloat(internal) * 0.5;
        score += extra * 2;
        score -= (parseFloat(internet) > 6 ? (parseFloat(internet) - 6) * 1.5 : 0);
        score += parents_edu * 2.5;
        score += parseFloat(income) * 0.0001;
        
        // Noise
        score += (Math.random() - 0.5) * 5;
        
        // Outliers
        if (Math.random() > 0.97) score += 15;
        if (Math.random() > 0.97) score -= 15;

        const final_score = Math.min(100, Math.max(0, score)).toFixed(1);

        csvContent += `${prev_marks},${attendance},${study_hours},${assignment},${internal},${extra},${internet},${parents_edu},${income},${final_score}\n`;
    }

    if (!fs.existsSync('public')) {
        fs.mkdirSync('public');
    }
    fs.writeFileSync('public/student_performance.csv', csvContent);
}

generateData();
console.log("CSV generated successfully.");
