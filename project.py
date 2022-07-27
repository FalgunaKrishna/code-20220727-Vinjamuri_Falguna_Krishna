from flask import Flask, Response, request, jsonify
application1 = Flask(__name__)
# data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
#         { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
#         { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
#         { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
#         {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
#         {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]


# 1)Calculate the BMI (Body Mass Index) using Formula 1, BMI Category and Health risk from Table 1 of the person and add them as 3 new columns
# 2)CountthetotalnumberofoverweightpeopleusingrangesinthecolumnBMICategory of Table 1, check this is consistent programmatically and add any other observations in the documentation


def calculate_BMI(data):
        for i in data:
                weight = i.get('WeightKg')
                height_mt = i.get('HeightCm') / 100  # change to meters
                bmi = weight / (height_mt ** 2)
                i.update({"BMI": bmi})
                # print(bmi)
                if bmi <= 18.4:
                        i.update({"BMI_Category": "Underweight"})
                        i.update({"Health_risk": "Malnutrition risk"})
                elif bmi >= 18.5 and bmi <= 24.9:
                        i.update({"BMI_Category": "Normal weight"})
                        i.update({"Health_risk": "Low risk"})
                elif bmi >= 25 and bmi <= 29.9:
                        i.update({"BMI_Category": "Overweight"})
                        i.update({"Health_risk": "Enhanced risk"})
                elif bmi >= 30 and bmi <= 34.9:
                        i.update({"BMI_Category": "Moderately obese"})
                        i.update({"Health_risk": "Medium risk"})
                elif bmi >= 35 and bmi <= 39.9:
                        i.update({"BMI_Category": "Severely obese"})
                        i.update({"Health_risk": "High risk"})
                elif bmi >= 40:
                        i.update({"BMI_Category": "Very severely obese"})
                        i.update({"Health_risk": "Very high risk"})

        over_weighted_count = 0
        for i in data:
                if 'Normal' not in i['BMI_Category'] and 'Under' not in i['BMI_Category']:
                        over_weighted_count += 1

        return {f"total_overweighted_persons:{over_weighted_count}"}


@application1.route('/get_bmi', methods=['POST'])
def get_bmi_details():
        request_data = request.json
        info = request_data.get("data")
        res = calculate_BMI(info)
        return Response(res, mimetype='application/json', status=200)

if __name__ == "__main__":
        application1.run(debug=True)