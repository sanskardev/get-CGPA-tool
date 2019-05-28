package com.example.mujresults;

import android.app.DatePickerDialog;
import android.app.Dialog;
import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.DialogFragment;

public class DatePickerFragment extends DialogFragment {

    @NonNull
    @Override
    public Dialog onCreateDialog(@Nullable Bundle savedInstanceState) {


        int year = 1999;
        int month = 0;
        int date = 1;

        return new DatePickerDialog(getActivity(), R.style.Theme_AppCompat_DayNight_Dialog_MinWidth, (DatePickerDialog.OnDateSetListener) getActivity(), year, month, date);

    }
}



