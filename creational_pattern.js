class GameSettings {
    constructor(settings) {
        if(GameSettings.instance) {
            return GameSettings.instance

        }
        this.settings = settings
        GameSettings.instance = true
    }
}

