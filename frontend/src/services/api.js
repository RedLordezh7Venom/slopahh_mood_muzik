const API_BASE_URL = 'http://localhost:8000/api/v1';

/**
 * Service to handle all interactions with the Mood Muzik Backend
 */
export const apiService = {
    /**
     * Fetches the list of predefined mood categories for the UI
     */
    async getMoods() {
        try {
            const response = await fetch(`${API_BASE_URL}/moods`);
            if (!response.ok) throw new Error('Failed to fetch moods');
            return await response.json();
        } catch (error) {
            console.error("API Error (getMoods):", error);
            throw error;
        }
    },

    /**
     * Sends user mood data (ID or text) to get song recommendations
     * @param {Object} payload { mood_id: string, text_input: string }
     */
    async getRecommendations(payload) {
        try {
            const response = await fetch(`${API_BASE_URL}/recommend`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(payload),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || 'Failed to get recommendations');
            }

            const data = await response.json();
            return data;
        } catch (error) {
            console.error("API Error (getRecommendations):", error);
            throw error;
        }
    },

    /**
     * Retrieves the recent mood history
     */
    async getHistory() {
        try {
            const response = await fetch(`${API_BASE_URL}/history`);
            if (!response.ok) throw new Error('Failed to fetch history');
            return await response.json();
        } catch (error) {
            console.error("API Error (getHistory):", error);
            throw error;
        }
    }
};
