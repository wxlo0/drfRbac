import { createStore } from 'vuex'
import TabsModule from './modules/tabs'
import CommonModule from './modules/common'
import createPersistedState from 'vuex-persistedstate'
import UserModule from './modules/user'

const store = createStore({
    modules: {
        tabs: TabsModule,
        common: CommonModule,
        user: UserModule
    },
    plugins: [createPersistedState()]
})

export default store
