<template>
    <div class="container">
        <h1 class="box">Login Form</h1>
        <form class="box" @submit.prevent="login">
            <!-- v-model: passing prop (modalValue) + listening to event (update:modalValue) and does the update -->
            <BaseInput type="email" id="email" label="Email" v-model="credentials.email"/>
            <BaseInput type="password" id="password" label="Password" v-model="credentials.password"/>
            <BaseButton type="submit" btn-class="primary" label="Submit" />
        </form>
        <div class="box mt-3">
            <p>Do not have an account ?</p>
            <p>Register as a <a href="#/register/company">Company</a></p>
            <p>Register as a <a href="#/register/student">Student</a></p>
        </div>
    </div>

</template>

<script>
import BaseInput from '@/components/BaseInput.vue';
import BaseButton from '@/components/BaseButton.vue';
import apiRequest from '@/apiRequest';

export default{
    components:{
        BaseInput,
        BaseButton
    },
    data(){
        return {
            credentials: {
                email: "",
                password: ""
            }
        }
    },
    methods:{
        async login(){
            const payload=this.credentials
            const data = await apiRequest('/auth/tokens','POST',payload)
            
            if (data.msg){
                return console.log(data.msg)
            }

            localStorage.setItem('token',data.token)

            switch (data.current_user_role) {
                case "admin":
                    window.location.hash = "#/admin/dashboard"
                    break;
                case "company":
                    window.location.hash = "#/company/dashboard"
                    break;
                case "student":
                    window.location.hash = "#/student/dashboard"
                    break;
                default:
                    console.log("error: USER ROLE IS NOT DEFINED!")
                    break;
            }
        }
    }
}
</script>