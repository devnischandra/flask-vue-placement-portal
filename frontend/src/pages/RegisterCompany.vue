<template>
    <div class="container">
        <h1 class="box">Register Company</h1>
        <form class="box">
            <!-- v-model: passing prop (modalValue) + listening to event (update:modalValue) and does the update -->
            <div class="row">
                <div class="col-6"><BaseInput type="text" id="name" label="Name" v-model="company.name"/></div>
                <div class="col-6"><BaseInput type="email" id="email" label="Email" v-model="company.email"/></div>
            </div>
            <div class="row">
                <div class="col-6"><BaseInput type="password" id="password" label="Password" v-model="company.password"/></div>
                <div class="col-6"><BaseInput type="number" max="10" id="hr_contact" label="HR Contact" v-model="company.hr_contact"/></div>
            </div>
            <BaseInput type="url" id="website_url" label="Website URL" v-model="company.website_url"/>
            <!-- submit-btn -->
            <BaseButton btn-type="primary" label="Submit" />
        </form>
        <div class="box mt-3">
            <p>Already have an account ? Click to: <a href="/">Login</a></p>
            <p>Click to register as: <a href="#/register-student">Student</a></p>
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
            company:{
                name:"",
                email:"",
                password:"",
                hr_contact:"",
                website_url:""
            }
        }
    }
}
</script>