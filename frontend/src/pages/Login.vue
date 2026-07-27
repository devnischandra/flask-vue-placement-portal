<template>
    <div class="container">
        <h1 class="box">Login Form</h1>
        <form class="box">
            <!-- v-model: passing prop (modalValue) + listening to event (update:modalValue) and does the update -->
            <BaseInput type="email" id="email" label="Email" v-model="email"/>
            <BaseInput type="password" id="password" label="Password" v-model="password"/>
            <BaseButton btn-type="primary" label="Submit" />
        </form>
        <div class="box mt-3">
            <p>Do not have an account ?</p>
            <p>Register as a <a href="#/register-company">Company</a></p>
            <p>Register as a <a href="#/register-student">Student</a></p>
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
            email: "",
            password: ""
        }
    }
}
</script>