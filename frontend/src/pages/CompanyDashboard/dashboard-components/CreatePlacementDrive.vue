<template>
    <form @submit.prevent="$emit('create-placement-drive', {...new_placement_drive})">
        <!-- v-model: passing prop (modalValue) + listening to event (update:modalValue) and does the update -->
        <div class="row">
            <div class="col-6"><BaseInput type="text" id="job_title" label="Job Title" v-model="new_placement_drive.job_title"/></div>
            <div class="col-6"><BaseInput type="numer" id="minimum_cgpa" label="Minimum CGPA Required" v-model="new_placement_drive.minimum_cgpa"/></div>
        </div>
        <div class="row">
            <div class="col-6"><BaseInput type="date" id="start_date" label="Start Date" v-model="new_placement_drive.start_date"/></div>
            <div class="col-6"><BaseInput type="date" id="end_date" label="End Date" v-model="new_placement_drive.end_date"/></div>
        </div>
        <BaseInput type="text" id="description" label="Description" v-model="new_placement_drive.description"/>
        <!-- Job Mode -->
        <div class="mb-3">
            <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" v-model="new_placement_drive.job_mode" id="office" value="office">
                <label class="form-check-label" for="office">Office</label>
            </div>
            <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" v-model="new_placement_drive.job_mode" id="remote" value="remote">
                <label class="form-check-label" for="remote">Remote</label>
            </div>
            <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" v-model="new_placement_drive.job_mode" id="hybrid" value="hybrid">
                <label class="form-check-label" for="hybrid">Hybrid</label>
            </div>
        </div>
        <BaseInput v-if="new_placement_drive.job_mode == 'hybrid' || new_placement_drive.job_mode == 'office'" 
        type="text" id="location" label="location" v-model="new_placement_drive.location"/>
        <!-- submit-btn -->
        <BaseButton type="submit" btn-class="primary" label="Submit" />
    </form>
</template>

<script>
import BaseInput from '@/components/BaseInput.vue';
import BaseButton from '@/components/BaseButton.vue';


export default {
    components:{
        BaseInput,
        BaseButton
    },
    emits:['create-placement-drive'],
    data(){
        return{
            new_placement_drive:{
                "job_title": "",
                "description": "",
                "job_mode": "",
                "location": "",
                "minimum_cgpa": 0,
                "start_date": "",
                "end_date": ""
            }
        }
    }
}
</script>