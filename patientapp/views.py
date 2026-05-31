from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from .forms import PatientForm
import pickle
import os

def predict_health(glucose, haemoglobin, cholesterol):

    try:
        model_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "ai_model",
            "model.pkl"
        )

        with open(model_path, "rb") as file:
            model = pickle.load(file)

        result = model.predict([
            [glucose, haemoglobin, cholesterol]
        ])

        return result[0]

    except Exception as e:
        return "Prediction Error"


def patient_list(request):

    patients = Patient.objects.all()

    return render(
        request,
        'patientapp/patient_list.html',
        {'patients': patients}
    )


def add_patient(request):

    if request.method == 'POST':

        form = PatientForm(request.POST)

        if form.is_valid():

            patient = form.save(commit=False)

            patient.remarks = predict_health(
                patient.glucose,
                patient.haemoglobin,
                patient.cholesterol
            )

            patient.save()

            return redirect('patient_list')

    else:

        form = PatientForm()

    return render(
        request,
        'patientapp/add_patient.html',
        {'form': form}
    )


def update_patient(request, pk):

    patient = get_object_or_404(
        Patient,
        pk=pk
    )

    if request.method == 'POST':

        form = PatientForm(
            request.POST,
            instance=patient
        )

        if form.is_valid():

            patient = form.save(commit=False)

            patient.remarks = predict_health(
                patient.glucose,
                patient.haemoglobin,
                patient.cholesterol
            )

            patient.save()

            return redirect('patient_list')

    else:

        form = PatientForm(instance=patient)

    return render(
        request,
        'patientapp/update_patient.html',
        {'form': form}
    )


def delete_patient(request, pk):

    patient = get_object_or_404(
        Patient,
        pk=pk
    )

    patient.delete()

    return redirect('patient_list')