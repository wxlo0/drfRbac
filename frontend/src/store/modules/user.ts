
interface UserState {
    token: null;
    username: string;
    real_name: string;
    role: string;
}

const UserModule = {
    state: {
        token: null,
        username: "",
        real_name: "",
        role: "",
    } as UserState,
    mutations: {
        setUserInfo(state: UserState, user_info: object) {
            state.token = user_info.token
            state.username = user_info.username
            state.real_name = user_info.real_name
            state.role = user_info.role
        }
    },
    actions: {},
    getters: {
        getToken(state: UserState) {
            return state.token
        }
    }
};

export default UserModule;
