"""APIs of video total counts application"""
from video_total_counts.models import VideoTotalCount


def increase_wish_count(video):
    """Increase wish_count of video's total count object"""
    _counter = video.videototalcount  # type: VideoTotalCount
    _counter.increase_wish_count()
    _counter.save()
    return _counter.wish_count


def decrease_wish_count(video):
    """Decrease wish_count of video's total count object"""
    _counter = video.videototalcount  # type: VideoTotalCount
    _counter.decrease_wish_count()
    _counter.save()
    return _counter.wish_count


def increase_watching_mark_count(video):
    """Increase watching_mark of video's total count object"""
    _counter = video.videototalcount  # type: VideoTotalCount
    _counter.increase_watch_count()
    _counter.save()
    return _counter.wish_count


def decrease_watching_mark_count(video):
    """Decrease watching_mark of video's total count object"""
    _counter = video.videototalcount  # type: VideoTotalCount
    _counter.decrease_watch_count()
    _counter.save()
    return _counter.wish_count
