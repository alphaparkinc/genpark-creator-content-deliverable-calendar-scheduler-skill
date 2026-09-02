from client import CreatorContentDeliverableCalendarSchedulerClient

def main():
    client = CreatorContentDeliverableCalendarSchedulerClient()
    res = client.schedule_campaign_calendar('Holiday_Gifting_2026', {'@style_guru': '2026-10-01'})
    print('Content Deliverable Calendar: ' + res['calendar_schedule_id'] + ' (' + res['campaign_name'] + ')')
    print('Posts Scheduled: ' + str(res['total_scheduled_posts_count']) + ' | Embargo Enforced: ' + str(res['embargo_blackout_windows_enforced']))
    print('Calendar URL: ' + res['interactive_content_calendar_url'])

if __name__ == '__main__':
    main()
