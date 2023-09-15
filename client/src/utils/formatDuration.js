export default function formatDuration(durationInMinutes) {
    const hours = Math.floor(durationInMinutes / 60);
    const minutes = durationInMinutes % 60;

    if (hours === 0) {
        return `${minutes}m`;
    } else {
        return `${hours}h ${minutes}m`;
    }
}