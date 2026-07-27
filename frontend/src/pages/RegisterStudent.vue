<template>
    <div class="container">
        <h1 class="box">Register Student</h1>
        <form class="box">
            <!-- v-model: passing prop (modalValue) + listening to event (update:modalValue) and does the update -->
            <div class="row">
                <div class="col-6"><BaseInput type="text" id="name" label="Name" v-model="student.name"/></div>
                <div class="col-6"><BaseInput type="email" id="email" label="Email" v-model="student.email"/></div>
            </div>
            <div class="row">
                <div class="col-6"><BaseInput type="password" id="password" label="Password" v-model="student.password"/></div>
                <div class="col-6"><BaseInput type="date" id="date_of_birth" label="Date of Birth" v-model="student.date_of_birth"/></div>
            </div>
            <div class="row">
                <div class="col-6"><BaseInput type="text" id="department" label="Department" v-model="student.department"/></div>
                <div class="col-6"><BaseInput type="number" id="cgpa" label="CGPA" v-model="student.cgpa"/></div>
            </div>
            <BaseInput type="url" id="resume_url" label="Resume URL" v-model="student.resume_url"/>
            <!-- GENDER -->
            <div class="mb-3">
                <div class="form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="student.gender" id="male" value="male">
                    <label class="form-check-label" for="male">Male</label>
                </div>
                <div class="form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="student.gender" id="female" value="female">
                    <label class="form-check-label" for="female">Female</label>
                </div>
                <div class="form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="student.gender" id="other" value="other">
                    <label class="form-check-label" for="other">Other</label>
                </div>
            </div>
            <!-- submit-btn -->
            <BaseButton btn-type="primary" label="Submit" />
        </form>
        <div class="box mt-3">
            <p>Already have an account ? Click to: <a href="/">Login</a></p>
            <p>Click to register as: <a href="#/register-company">Company</a></p>
        </div>  
    </div>

</template>

<script>
import BaseInput from '@/components/BaseInput.vue';
import BaseButton from '@/components/BaseButton.vue';

export default{
    components:{
        BaseInput,
        BaseButton
    },
    data(){
        return {
            student:{
                name:"",
                email:"",
                password:"",
                gender:"",
                date_of_birth:"",
                department:"",
                cgpa:"",
                resume_url:""
            }
        }
    }
}
</script>