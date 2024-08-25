// Function to get URL query parameters
function getQueryParams() {
    const params = new URLSearchParams(window.location.search);
    return {
	name: params.get('name') || 'Guest',  // Default value if parameter is missing
        gender: params.get('gender') || 'Unknown',
        relationshipStatus: params.get('relationshipStatus') || 'Unknown',
        genderPreference: params.get('genderPreference') || 'Any'
    };
}

// Display the results
document.addEventListener('DOMContentLoaded', () => {
    const params = getQueryParams();
    const message = `Welcome ${params.name}! Here are the preferences you're looking for: Gender ${params.genderPreference} that are looking for ${params.relationshipStatus}.`;
    document.getElementById('responseMessage').textContent = message;
});
